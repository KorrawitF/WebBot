# WebBot

A Selenium bot that logs into a class-booking website, opens a chosen plan, and races to claim a schedule slot the moment registration opens.

Two variants are included: one that starts immediately, and one that waits for a wall-clock time before submitting.

## What's in here

| File | Description |
| --- | --- |
| `RegisterWebBot(No timer).py` | Logs in and registers as soon as the page is ready; runs headless |
| `RegisterWebBot(Timer).py` | Same flow, but blocks until a configured `HH:MM:SS` before clicking register |

## How it works

The flow is split into four stages that call one another and retry recursively on failure, so a slow-loading page simply causes another attempt rather than a crash:

1. **`Logger()`** — fills the username and password fields and submits the login form.
2. **`FindPlan()`** — clicks the target plan by XPath and waits for the schedule content to load.
3. **`Regist()`** — clicks the schedule slot, confirms in the SweetAlert modal, and detects the error icon. On an error the modal is dismissed and the attempt repeats; on success it moves on.
4. **`Success()`** — reports the booking and stops.

The timer variant spins on `time.strftime("%H:%M:%S")` inside `Regist()` until the configured moment, so login and navigation are already finished when the slot opens.

`webdriver_manager` downloads a matching ChromeDriver automatically.

## Requirements

```bash
pip install selenium webdriver-manager
```

Google Chrome installed.

## Configuration

Both scripts have a block of blank constants near the top that must be filled in:

```python
username        = ""   # your login
password        = ""   # your password
planXpath       = ""   # XPath of the plan to open
scheduleSelector= ""   # CSS selector of the slot to book
Timers          = [True, "14:44:58"]   # timer version only: when to fire
driver.get("")         # the target site
```

## Run

```bash
python "RegisterWebBot(Timer).py"
```

## Notes

- Written against Selenium 3's `find_element_by_*` API; Selenium 4 removed those methods, so pin `selenium<4` or update the calls to `find_element(By.X, ...)`.
- Every selector is a brittle absolute XPath tied to one specific site layout.
- Automating a booking site may violate its terms of service — use only where you are permitted to.
