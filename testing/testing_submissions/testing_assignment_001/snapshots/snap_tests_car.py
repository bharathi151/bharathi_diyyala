# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_object_creation_with_invalid_max_speed_raise_value_error[red--100-10-3] Invalid value for max_speed'] = 'Invalid value for max_speed'

snapshots['test_object_creation_with_invalid_max_speed_raise_value_error[red-0-10-3] Invalid value for max_speed'] = 'Invalid value for max_speed'

snapshots['test_object_creation_with_invalid_acceleration_raise_value_error[red-100--10-3] Invalid value for acceleration'] = 'Invalid value for acceleration'

snapshots['test_object_creation_with_invalid_acceleration_raise_value_error[red-100-0-3] Invalid value for acceleration'] = 'Invalid value for acceleration'

snapshots['test_object_creation_with_invalid_tyre_friction_raise_value_error[red-100-10--3] Invalid value for tyre_friction'] = 'Invalid value for tyre_friction'

snapshots['test_object_creation_with_invalid_tyre_friction_raise_value_error[red-100-10-0] Invalid value for tyre_friction'] = 'Invalid value for tyre_friction'

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] is_instance'] = True

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] max_speed'] = 2

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] tyre_friction'] = 1

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] acceleration'] = 1

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] is_engine_started'] = False

snapshots['test_object_creation_with_valid_details_rerurn_car_object[red-2-1-1] current_speed'] = 0

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] is_instance'] = True

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] max_speed'] = 2

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] tyre_friction'] = 1

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] acceleration'] = 1

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] is_engine_started'] = False

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-2-1-1] current_speed'] = 0

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] is_instance'] = True

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] max_speed'] = 3

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] tyre_friction'] = 1

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] acceleration'] = 1

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] is_engine_started'] = False

snapshots['test_multiple_objects_creation_with_valid_details_return_car_objects[red-3-1-1] current_speed'] = 0

snapshots['test_start_engine_first_time_returns_is_engine_true[red-1-1-1] is_engine_started'] = True

snapshots['test_current_speed_when_start_engine_called_twice_return_is_engine_started_true[red-1-1-1] is_engine_started'] = True

snapshots['test_sound_horn_when_car_engine_is_not_started_return_warn[red-1-1-1] is_engine_started'] = False

snapshots['test_sound_horn_when_car_engine_is_started_returns_sound[red-1-1-1] is_engine_started'] = True

snapshots['test_accelerate_before_engine_starts_returns_error[red-1-1-1] is_engine_started'] = False

snapshots['test_stop_engine_when_car_is_not_running_returns_is_engine_started_false is_engine_started'] = False

snapshots['test_stop_engine_when_car_is_running_returns_is_engine_started_false is_engine_started'] = False

snapshots['test_apply_breaks_before_engine_starts_zero_current_speed is_engine_started'] = False

snapshots['test_apply_breaks_before_engine_starts_zero_current_speed current_speed'] = 0

snapshots['test_apply_breaks_after_engine_starts_return_updated_current_speed is_engine_started'] = True

snapshots['test_apply_breaks_after_engine_starts_return_updated_current_speed current_speed'] = 0

snapshots['test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed is_engine_started'] = True

snapshots['test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed current_speed'] = 10

snapshots['test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed is_engine_started'] = True

snapshots['test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed current_speed'] = 20

snapshots['test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed is_engine_started'] = True

snapshots['test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed current_speed'] = 20

snapshots['test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed is_engine_started'] = True

snapshots['test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed current_speed'] = 0

snapshots['test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed is_engine_started'] = True

snapshots['test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed current_speed'] = 7

snapshots['test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed is_engine_started'] = True

snapshots['test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed current_speed'] = 0

snapshots['test_sound_horn_when_car_engine_is_not_started_return_warn[red-1-1-1] warn for start_engine'] = True

snapshots['test_sound_horn_when_car_engine_is_started_returns_sound[red-1-1-1] horn_sound'] = '''Beep Beep
'''

snapshots['test_accelerate_before_engine_starts_returns_error[red-1-1-1] warn for start_engine'] = True

snapshots['test_acceleraton_encaspulation_returns_updated_acceleration error_message'] = "can't set attribute"

snapshots['test_tyre_friction_encaspulation_returns_updated_tyre_friction error_message'] = "can't set attribute"

snapshots['test_max_speed_encaspulation_returns_updated_max_speed error_message'] = "can't set attribute"

snapshots['test_current_speed_encaspulation_returns_updated_current_speed error_message'] = "can't set attribute"

snapshots['test_color_encaspulation_returns_updated_color error_message'] = "can't set attribute"
