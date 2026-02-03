\# Data Structures (MongoDB Documents)



\## users

| Field      | Type     | Description              |

|------------|----------|--------------------------|

| \_id        | ObjectId | Unique MongoDB id        |

| username   | string   | User name (unique)       |

| email      | string   | User email (unique)      |

| created\_at | datetime | Creation timestamp       |



\## datasets

| Field      | Type     | Description              |

|------------|----------|--------------------------|

| \_id        | ObjectId | Unique MongoDB id        |

| name       | string   | Dataset name             |

| path       | string   | File path                |

| uploaded\_at| datetime | Upload timestamp         |



\## quality\_reports

| Field         | Type          | Description                        |

|---------------|---------------|------------------------------------|

| \_id           | ObjectId      | Unique MongoDB id                  |

| user\_id       | ObjectId      | Reference to user                  |

| dataset\_id    | ObjectId      | Reference to dataset               |

| checked\_at    | datetime      | Report creation time               |

| column\_checks | list\[dict]    | Each dict: column\_name + null\_count|

