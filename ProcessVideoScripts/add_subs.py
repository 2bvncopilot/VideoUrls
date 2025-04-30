import subprocess

def add_subtitles(input_video, input_srt, output_video):
    """
    Adds subtitles to a video using FFmpeg
    :param input_video: Path to input video file
    :param input_srt: Path to SRT subtitle file
    :param output_video: Path for output video
    """
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-vf', f"subtitles={input_srt}:force_style='Fontsize=15,PrimaryColour=&H00FF00&,MarginV=50'",
        '-c:a', 'copy',
        output_video
    ]
    subprocess.run(cmd, check=True)

# Example usage
add_subtitles('/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/input.mp4', '/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/subtitle.srt', '/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/output.mp4')

# import subprocess

# def add_dual_subtitles(input_video, input_srt_vn, output_video):
#     """
#     Adds two subtitle tracks (Vietnamese bottom, English top) burned into the video using FFmpeg
#     :param input_video: Path to input video file
#     :param input_srt_vn: Path to Vietnamese SRT subtitle file
#     :param output_video: Path for output video
#     """
#     cmd = [
#         'ffmpeg',
#         '-i', input_video,
#         '-filter_complex',
#         f"[0:v]subtitles='{input_srt_vn}':force_style='Fontsize=15,PrimaryColour=&H00FF00,MarginV=50'",
#         '-map', '[v]',
#         '-map', '0:a?',
#         '-c:v', 'libx264',
#         '-c:a', 'copy',
#         output_video
#     ]
#     subprocess.run(cmd, check=True)

# # Example usage
# add_dual_subtitles(
#     '/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/input.mp4',
#     '/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/vi.srt',
#     '/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/output.mp4'
# )
