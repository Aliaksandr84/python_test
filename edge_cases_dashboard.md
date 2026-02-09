1\. No Uploads Yet

Edge Case:

A brand new user visits the dashboard with no CSV files ever uploaded.





Why:

The dashboard shouldn’t throw errors, should display a “no uploads yet” message, and hide or gray out links to reports.





2\. Corrupted or Incomplete Upload Metadata

Edge Case:

An upload is recorded in the database, but its corresponding CSV or report is missing/corrupted (e.g., file deleted, crashed during file write).





Why:

The dashboard should degrade gracefully, showing status (e.g., “file missing”), not attempt to link to a broken report, and possibly offer re-upload.





3\. User Uploads Massive CSV—Summary Metrics Timeout

Edge Case:

A single CSV upload is so large that summary metrics (number of rows, columns, issues) take too long to calculate or cause a timeout.





Why:

Dashboard should handle this by showing a loading state or “processing in background,” not a broken widget.





4\. Duplicate Filenames in Upload History

Edge Case:

Multiple users, or the same user, upload files with identical filenames (e.g., data.csv).





Why:

The dashboard must differentiate these (by upload date/time, user, or internal ID) and not overwrite or conflate history entries.





5\. Timezone Mismatches for Timestamps

Edge Case:

Uploads happen from users in different timezones, or the server time shifts (e.g., with Daylight Saving).





Why:

Dashboard should consistently display times in UTC, user’s local timezone, or clearly labeled, avoiding confusion on “recent uploads."





6\. Partial or Disjoint Report Data

Edge Case:

For an upload, some, but not all, quality checks complete (e.g., missing value check runs; outlier detection fails due to a bug or resource limit).





Why:

Dashboard must present partial results with clear indication of what succeeded/failed, not an all-or-nothing display.





7\. Orphaned Reports

A report exists with no associated (orphaned) upload record due to manual changes or bugs. The dashboard should not display these, or should show a warning for admin attention.







