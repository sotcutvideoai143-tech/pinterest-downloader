Pinterest Video Downloader — Backend ফাইল

সত্যি কথা: ZIP ফাইল আপলোড করলেই API নিজে থেকে চালু হবে না। API-টি একটি backend hosting service-এ deploy করতে হবে, তারপর index.html-এ API URL বসিয়ে Netlify-তে আবার deploy করতে হবে।

ফাইলগুলো:
- app.py: ভিডিও আনার API
- requirements.txt: Python package
- Dockerfile: backend deploy করার ফাইল
- render.yaml: Render config
- index.html: ওয়েবসাইটের পেজ

সেটআপের সংক্ষিপ্ত ধাপ:
1. এই ZIP-টি GitHub repository-তে আপলোড করুন।
2. Render-এ account খুলে New → Web Service দিয়ে repository-টি connect করুন। Docker runtime নির্বাচন করুন; free plan থাকলে সেটি নিন।
3. Deploy শেষ হলে Render-এর service URL কপি করুন (যেমন https://your-service.onrender.com)। Free service ঘুমিয়ে যেতে পারে এবং পরে চালু হতে সময় লাগতে পারে।
4. index.html ফাইলে API_BASE = 'PASTE_YOUR_RENDER_API_URL_HERE' লাইনে placeholder-এর জায়গায় নিজের Render URL বসান।
5. index.html-টি আপনার Netlify সাইটে নতুন করে deploy করুন।

গুরুত্বপূর্ণ:
- বিনামূল্যের hosting-এর স্থায়িত্ব/সীমা নিশ্চিত নয়।
- Pinterest লিংক সবসময় কাজ নাও করতে পারে; private, login-প্রয়োজনীয় বা সীমাবদ্ধ ভিডিও নামবে না।
- শুধু নিজের ব্যবহারের অধিকার আছে এমন ভিডিও ডাউনলোড করুন এবং Pinterest-এর নিয়ম মানুন।
