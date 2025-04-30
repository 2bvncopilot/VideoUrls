import whisper
from moviepy import VideoFileClip
import os

def ms_to_srt_time(seconds):
    """Convert seconds to SRT time format (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}".replace(".", ",")

def split_text_into_lines(text, max_line_length=40):
    """Split a long text into multiple lines, each with a max length of `max_line_length`."""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        # If adding the word exceeds max line length, start a new line
        if len(" ".join(current_line + [word])) > max_line_length:
            lines.append(" ".join(current_line))
            current_line = [word]  # Start a new line with the current word
        else:
            current_line.append(word)
    
    # Add any remaining words to the last line
    if current_line:
        lines.append(" ".join(current_line))
    
    return lines

def transcribe_to_srt(input_mp4, output_en_srt):
    try:
        # Step 1: Extract audio (Whisper works better with WAV)
        audio_temp = "temp_audio.wav"
        video_clip = VideoFileClip(input_mp4)
        video_clip.audio.write_audiofile(audio_temp, codec='pcm_s16le')

        # Step 2: Transcribe English audio with Whisper
        model = whisper.load_model("base")  # Use "small", "medium" for better accuracy
        result = model.transcribe(audio_temp)

        # Step 3: Write English SRT file
        with open(output_en_srt, "w", encoding="utf-8") as f_en:
            idx = 1
            for segment in result["segments"]:
                # Split long subtitles into shorter lines (max 40 characters per line)
                lines = split_text_into_lines(segment["text"])

                # Write each line of the subtitle to the SRT file
                for line in lines:
                    f_en.write(f"{idx}\n")
                    f_en.write(f"{ms_to_srt_time(segment['start'])} --> {ms_to_srt_time(segment['end'])}\n")
                    f_en.write(f"{line}\n\n")
                    idx += 1

        print(f"English subtitles successfully saved to {output_en_srt}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        # Cleanup
        if os.path.exists(audio_temp):
            os.remove(audio_temp)

# Usage
transcribe_to_srt(
    input_mp4="/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/input.mp4",
    output_en_srt="/Users/WORK/HOME/MY_APPS/VideoUrls/ProcessVideoScripts/en.srt"
)
