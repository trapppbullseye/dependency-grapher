#!/usr/bin/env python3
"""Graph repo dependency tree per commit"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Graph repo dependency tree per commit")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("dependency-grapher v0.1.0");return
 print(f"[12:00] dependency-grapher ready")
if __name__=="__main__":main()
