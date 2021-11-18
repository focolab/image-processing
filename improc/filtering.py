import numpy as np

"""
Get the MIP across a temporal window around the requested frame. Where requested frame is too early or late
for the requested window size, the temporal window will be truncated as necessary.
"""
def get_tmip(mft, frame, num_frames=11):
    start_frame = max(0, frame - num_frames // 2)
    stop_frame = min(max(mft.indexing.keys()), frame + num_frames // 2)
    frame_indices = list(range(start_frame, stop_frame + 1))
    frames = mft.get_frames(frame_indices)
    return np.max(frames, axis=0)

"""
Get the average across a temporal window around the requested frame. Where requested frame is too early or late
for the requested window size, the temporal window will be truncated as necessary.
"""
def get_tavg(mft, frame, num_frames=11):
    start_frame = max(0, frame - num_frames // 2)
    stop_frame = min(max(mft.indexing.keys()), frame + num_frames // 2)
    frame_indices = list(range(start_frame, stop_frame + 1))
    frames = mft.get_frames(frame_indices)
    return np.mean(frames, axis=0)
