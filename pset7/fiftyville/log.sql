-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Query to get a description of crime scene reports from the day of the roberry
SELECT description FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

-- Query to get the transcripts of the witnesses that have the word bakery from the day of the robbery
SELECT transcript FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

-- Query to give names of people that exited the bakery within 10 minutes of the robbery
SELECT name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit";

-- Query to get names of people that made withdrawals from the atm at Lenggett Street on the day of the roberry
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";

-- Query to find fiftyville in airports
SELECT * FROM airports;

-- Query to explore for first flight out of Fiftyville
SELECT f.*, origin.full_name AS origin_airport, destination.full_name AS destination_airport FROM flights f
JOIN airports origin ON f.origin_airport_id = origin.id
JOIN airports destination ON f.destination_airport_id = destination.id
WHERE origin.id = 8 AND f.year = 2021 AND f.month = 7 AND f.day = 29
ORDER BY f.hour, f.minute
LIMIT 1;

--Query to get the caller
SELECT name FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

--Query to get the receiver
SELECT phone_number FROM people
WHERE name = "Bruce";
SELECT name FROM people
WHERE phone_number = (
    SELECT receiver FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = "(367) 555-5533"
);
