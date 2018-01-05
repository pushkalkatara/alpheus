;; Auto-generated. Do not edit!


(when (boundp 'alpheus_actions::depthGoal)
  (if (not (find-package "ALPHEUS_ACTIONS"))
    (make-package "ALPHEUS_ACTIONS"))
  (shadow 'depthGoal (find-package "ALPHEUS_ACTIONS")))
(unless (find-package "ALPHEUS_ACTIONS::DEPTHGOAL")
  (make-package "ALPHEUS_ACTIONS::DEPTHGOAL"))

(in-package "ROS")
;;//! \htmlinclude depthGoal.msg.html


(defclass alpheus_actions::depthGoal
  :super ros::object
  :slots (_depth_setpoint ))

(defmethod alpheus_actions::depthGoal
  (:init
   (&key
    ((:depth_setpoint __depth_setpoint) 0.0)
    )
   (send-super :init)
   (setq _depth_setpoint (float __depth_setpoint))
   self)
  (:depth_setpoint
   (&optional __depth_setpoint)
   (if __depth_setpoint (setq _depth_setpoint __depth_setpoint)) _depth_setpoint)
  (:serialization-length
   ()
   (+
    ;; float32 _depth_setpoint
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _depth_setpoint
       (sys::poke _depth_setpoint (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _depth_setpoint
     (setq _depth_setpoint (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get alpheus_actions::depthGoal :md5sum-) "eac9b1c2b936598b47862f11c21394fc")
(setf (get alpheus_actions::depthGoal :datatype-) "alpheus_actions/depthGoal")
(setf (get alpheus_actions::depthGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
float32 depth_setpoint

")



(provide :alpheus_actions/depthGoal "eac9b1c2b936598b47862f11c21394fc")

