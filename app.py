import os, tempfile, shutil
from flask import Flask, request, send_file, jsonify
import yt_dlp

app = Flask(__name__)

@app.get('/')
def home():
    return jsonify({"service":"Pinterest Video Downloader API","status":"running"})

@app.post('/download')
def download():
    data = request.get_json(silent=True) or request.form
    url = (data.get('url') or '').strip()
    if not url.startswith(('https://', 'http://')) or 'pinterest.' not in url.lower():
        return jsonify({"error":"সঠিক Pinterest ভিডিও লিংক দিন।"}), 400
    folder = tempfile.mkdtemp(prefix='pin_dl_')
    try:
        opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': os.path.join(folder, '%(title).80s.%(ext)s'),
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'restrictfilenames': True,
            'socket_timeout': 25,
            'max_filesize': 150 * 1024 * 1024,
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            path = ydl.prepare_filename(info)
            if not os.path.exists(path):
                # Some extractors change the extension after merging.
                base = os.path.splitext(path)[0]
                matches = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and os.path.splitext(os.path.join(folder, f))[0] == base]
                if matches: path = matches[0]
            if not os.path.exists(path):
                files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
                if not files: raise RuntimeError('ভিডিও ফাইল পাওয়া যায়নি।')
                path = files[0]
            return send_file(path, as_attachment=True, download_name=os.path.basename(path), mimetype='video/mp4')
    except Exception as e:
        shutil.rmtree(folder, ignore_errors=True)
        return jsonify({"error":"ভিডিও পাওয়া যায়নি। Pinterest লিংকটি public কি না দেখুন, পরে আবার চেষ্টা করুন।", "details": str(e)[:300]}), 502

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '8080')))
