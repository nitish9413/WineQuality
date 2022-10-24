import os
from pickletools import read_uint1
import sys

class wineException:
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message = wineException.get_detailed_error_message(
            error_message=error_message,
            error_details=error_details
        )

    @staticmethod
    def get_detailed_error_message(
        error_message:Exception,
        error_detail:sys
        )->str:
        """
        Error_message : Excepiton Object
        Error_detail : Object of sys module 
        """

        _,_,exec_tb = error_detail.exc_info()
        exception_block_line_number = exec_tb.tb_frame.f_lineno
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error Occured in script :
        [ {file_name} ] at 
        try block line number : [{ try_block_line_number}] and
        exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        """

        return error_message
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return wineException.__name__.str()