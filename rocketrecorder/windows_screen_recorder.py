import datetime
import platform

if platform.system() == "Windows":
    from screen_recorder_sdk import screen_recorder


def record():
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


def stop_video_recording():
    """
    Stop the screen recording based on the platform.
    """
    screen_recorder.stop_video_recording()
    free_resources()


def free_resources():
    """
    Free the resources used by the screen_recorder_sdk.
    """
    screen_recorder.free_resources()
