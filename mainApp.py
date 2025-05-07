from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get_video_url():
    try:
        url = request.args.get('url')
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'format': 'best[height<=720]/best',
            'cookiefile': 'www.youtube.com_cookies.txt',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return jsonify({
            'title': info.get('title'),
            'url': info.get('url'),
            'ext': info.get('ext')
        })
    except Exception as e:
        return jsonify({
            'title': '',
            'url': '',
            'ext': '',
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
