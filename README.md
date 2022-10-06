Kuka LWR 4+ Description
================

This package contains the URDF (with inertia matrices) for the Kuka LWR 4+ at ISIR.

```bash
# Upload the robot description in the parameter server
ros2 launch lwr_description lwr_upload.launch.py
# Launch the fake robot in rviz (to debug)
ros2 launch lwr_description lwr_test.launch.py
```

> Author: Antoine Hoarau <hoarau.robotics@gmail.com>
