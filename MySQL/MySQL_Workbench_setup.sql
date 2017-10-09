{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11100\viewh8700\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 USE tweeter;\
\
SELECT * FROM faves;\
\
INSERT INTO users (first_name, last_name, birthday, created_at, updated_at) VALUES\
(\'91Joy\'92, \'91Joo\'92, 1987-02-11, NOW(), NOW());\
\
DELETE FROM users WHERE id = 1;\
UPDATE users SET first_name = \'91Kobe\'92 WHERE ID id = 1; }