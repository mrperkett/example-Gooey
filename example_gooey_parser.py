#! /usr/bin/env python3
"""
A test script demonstrating how to use Gooey.  This script collects the information
that you would need to send a coworker scheduled emails, but it just prints to screen
rather than spamming someone. :)
"""

import argparse
import datetime
import logging
import os
import sys
import time

from gooey import Gooey, GooeyParser


@Gooey(program_name="My Widget Example")
def main():
    """
    """
    # set up logging 
    logging.basicConfig(level=logging.DEBUG)
#    logging.basicConfig(filename="test_simple.log", level=logging.DEBUG)

    # Parse arguments
    parser = GooeyParser(description="Script to test Gooey's functionality")
    parser.add_argument("--name", 
                        "-n", 
                        type=str,
                        choices=["Steve", "Jesse", "Matt", "Tiana", "John P", "John M", "Rick", "Annaleen"],
                        required=True,
                        default="Matt",
                        help="Name of team member to send email(s)")

    parser.add_argument("Message", 
                        help="File containing message to be sent.", 
                        widget="FileChooser")

    parser.add_argument("--subject", 
                        type=str,
                        required=False,
                        help="Subject line of email")

    parser.add_argument("Log Directory", 
                        help="Directory for logging",
                        default=os.getcwd(), 
                        widget="FileChooser")

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    parser.add_argument("Start Date",
                        help="",
                        default=tomorrow,
                        widget="DateChooser")

    time_choices = [f"{hour}:{minute}{am_pm}" for am_pm in ("AM", "PM") for hour in (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) for minute in ("00", "30")] 

    parser.add_argument("--start_time",
                        type=str,
                        choices=time_choices,
                        required=True,
                        default="9:00AM",
                        help="Start time for emails")

    parser.add_argument("--num-emails",
                        "-ne",
                        type=int,
                        required=False,
                        default=1,
                        help="How many emails should be sent")

    parser.add_argument("--spacing",
                        "-s",
                        type=int,
                        required=False,
                        default=2,
                        help="Time between emails being sent (in hours)")

    parser.add_argument("--limit_hours_sent",
                        action="store_true",
                        default=True,
                        help="Only send emails during business hours")

    args = parser.parse_args()


    # Check input
    if args.num_emails <= 0:
        raise ValueError(f"num_emails ({args.num_emails}) must be > 0")

    if args.spacing < 0.0:
        raise ValueError(f"spacing ({args.spacing}) must be >= 0.0")

 
    # Schedule the emails
    # NOTE: this toy example has no code for this :)
    logging.info("Job successfully scheduled!")
   
 
    return


if __name__ == "__main__":
    main()
