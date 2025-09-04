class FlashForgeCommands:
    request_control_message = '~M601 S1\r\n'
    request_info_message = '~M115\r\n'
    request_head_position = '~M114\r\n'
    request_temp = '~M105\r\n'
    request_progress = '~M27\r\n'
    request_status = '~M119\r\n'

    led_on = "~M146 r255 g255 b255 F0"
    led_off = "~M146 r0 g0 b0 F0"
    save_file = "~M29\r"

    move_home = "~G28\r"

    set_absolute_home = "~G91\r"
    set_absolute_move = "~G90\r"

    stop_print = "~M26\r"

    pause_print = "~M25\r"

    def move_xyz(self, x: int = None, y: int = None, z: int = None):
        move = "~G1"
        if x is not None:
            move += f" X{x}"
        if y is not None:
            move += f" Y{y}"
        if z is not None:
            move += f" Z{z}"
        if move == "~G1":
            raise ValueError
        move += "\r"
        return move
    
    def prepare_print(file_size: int, filename: str = "file.gx"):
        return f"~M28 {file_size} 0:/user/{filename}\r"
    
    def start_print(filename: str = "file.gx"):
        return f"~M23 0:/user/{filename}\r"
    
    def delete_file(filename: str):
        return f"~M30 0:/user/{filename}"
    

        
