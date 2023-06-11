import datetime
import platform

if platform.system() == "Linux":
    import subprocess


def record():
    """
    Record the screen using ffmpeg on Linux.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"video_{timestamp}.mp4"

    subprocess.run(
        [
            "ffmpeg",
            "-video_size",
            "1920x1080",
            "-framerate",
            "30",
            "-f",
            "x11grab",
            "-i",
            ":0.0",
            file_name,
        ]
    )


def stop_video_recording():
    """
    Stop the screen recording based on the platform.
    """
    subprocess.run(["pkill", "ffmpeg"])
