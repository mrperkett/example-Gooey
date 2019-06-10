#! /usr/bin/env python3
"""
A test script demonstrating how to use Gooey.  This script collects the information
that you would need to send a coworker scheduled emails, but it just prints to screen
rather than spamming someone. :)
"""

import argparse
import logging
import os
import sys
import time

from gooey import Gooey


EMAILS_BY_NAME = {"Steve" : "steve_email_address",
                    "Jesse" : "jesse_email_address",
                    "Matt" : "matt_email_address",
                    "Tiana" : "tiana_email_address",
                    "John" : "john_email_address",
                    "Rick" : "rick_email_address",
                    "Annaleen" : "annaleen_email_address"}


def send_emails(email_address, message="Test", num_emails=1, delay=10.0, spacing=30.0):
    """
    Send email(s) to email address.  (well, in reality, just print to console for each email)

    Args:
    	email_address (str): address to which email(s) will be sent
    	message (str): body text for email
    	num_emails (int): number of emails to be sent
    	delay (float): how long to wait before sending first email (in seconds)
    	spacing (float): how long to wait between sending emails (in seconds)

    Return:
    	None
    """
    logging.info(f"Sending {num_emails} email(s) spaced by {spacing} seconds to {email_address} starting in {delay} seconds...")

    time.sleep(delay)

    for i in range(num_emails):
        # clearly this is where you would insert the actual code to send an email
        logging.info(f"\tSent email {i}.")

        if i < num_emails - 1:
            time.sleep(spacing)

    logging.info("Done.")

    return


@Gooey
def main():
    """
    """
    # set up logging 
    logging.basicConfig(level=logging.DEBUG)
#    logging.basicConfig(filename="test_simple.log", level=logging.DEBUG)

    # Parse arguments
    parser = argparse.ArgumentParser(description="Script to test Gooey's functionality")
    parser.add_argument("--name", 
                        "-n", 
                        type=str,
                        choices=["Steve", "Jesse", "Matt", "Tiana", "John", "Rick", "Annaleen"],
                        required=True,
                        default="Matt",
                        help="Name of team member to send email(s)")

    parser.add_argument("--message",
                        "-m",
                        type=str,
                        required=True,
                        default="Test Message",
                        help="Message in email")

    parser.add_argument("--num-emails",
                        "-ne",
                        type=int,
                        required=False,
                        default=1,
                        help="How many emails should be sent")

    parser.add_argument("--delay",
                        "-d",
                        type=float,
                        required=False,
                        default=2.0,
                        help="How long to wait before sending first email (in seconds)")

    parser.add_argument("--spacing",
                        "-s",
                        type=float,
                        required=False,
                        default=2.0,
                        help="Time between emails being sent (in seconds)")

    args = parser.parse_args()


    # Check input
    if args.num_emails <= 0:
        raise ValueError(f"num_emails ({args.num_emails}) must be > 0")

    if args.delay < 0.0:
        raise ValueError(f"delay ({args.delay}) must be >= 0.0")

    if args.spacing < 0.0:
        raise ValueError(f"spacing ({args.spacing}) must be >= 0.0")
   
 
    # Send the emails
    send_emails(EMAILS_BY_NAME[args.name],
                message=args.message,
                num_emails=args.num_emails,
                delay=args.delay,
                spacing=args.spacing)
   
 
    return


if __name__ == "__main__":
    main()
