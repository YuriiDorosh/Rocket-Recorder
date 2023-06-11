import datetime
import subprocess
import platform
from screen_recorder_sdk import screen_recorder


def record_windows():
    """
    Record the screen using the screen_recorder_sdk on Windows.
    """
    screen_recorder.enable_dev_log()
    params = screen_recorder.RecorderParams()
    screen_recorder.init_resources(params)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"video_{timestamp}.mp4"
    screen_recorder.start_video_recording(
        os.path.join(f"{file_name}"), 30, 8000000, True
    )


def record_linux():
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
    Stop the video recording using the screen_recorder_sdk.
    """
    screen_recorder.stop_video_recording()
    screen_recorder.free_resources()


def free_resources():
    """
    Free the resources used by the screen_recorder_sdk.
    """

