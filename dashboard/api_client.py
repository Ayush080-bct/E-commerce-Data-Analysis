"""
Thin client for the fastapi backend, shared by everypage.
Nothing in here renders ui - it only fetches/parses data.
"""

import os
import pandas as pd
import requests
import streamlit as st