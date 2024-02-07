# Silly Status

Silly Status is an advanced monitoring bot designed to oversee the operational status of the "Silly-Bot" within a Discord server. By tracking the target bot's presence and broadcasting updates through designated channels, Silly Status serves as an essential tool for maintaining awareness of the bot's availability and ensuring prompt notifications in case of downtime.

<a href="https://twitch.tv/sillysoon" target="_blank">![Static Badge](https://img.shields.io/badge/SillySoon-9145ff?style=for-the-badge&logo=twitch&logoColor=white)</a>
<a href="https://discord.gg/FEdbHTXVFn">![Static Badge](https://img.shields.io/badge/Support-4f63f0?style=for-the-badge&logo=discord&logoColor=white)</a>
<a href="https://github.com/SillySoon/silly-status/blob/main/LICENSE" target="_blank"> ![](https://img.shields.io/npm/l/silly-logger?style=for-the-badge&color=c759e5&labelColor=ca64e7) </a>
<a href="https://github.com/SillySoon" target="_blank"> ![](https://img.shields.io/github/followers/sillysoon?labelColor=d2d1d1&color=2f2f2f&logo=github&logoColor=2f2f2f&style=for-the-badge)</a>

## Features

- **Real-Time Monitoring**: Tracks the online and offline status of Silily-Bot, providing immediate updates.
- **Custom Notifications**: Sends customized messages to a specified channel and directly notifies a user when the bot goes offline.
- **Announcement Channel Integration**: For updates sent to announcement channels, messages are automatically published to maximize visibility.
- **Dynamic Presence**: Adjusts its own Discord presence based on the target bot's status, offering at-a-glance insight into the system's current state.

## Installation

### Prerequisites

- Python 3.6 or higher.
- `discord.py` library with intents enabled.
- A `.env` file configured with necessary tokens and IDs.

### Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/SillySoon/silly-status
   cd silly-status
   ```

2. **Environment Configuration**:
   - Create a `.env` file in the `src` directory using the `.env.template` as a guide.
   - Provide values for `BOT_TOKEN`, `NOTIFY_CHANNEL_ID`, `TARGET_BOT_ID`, `NOTIFY_USER_ID`, and `BOT_GUILD`.

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Launch the Bot**:
   ```sh
   cd src
   python bot.py
   ```

## Configuration

Ensure your `.env` file contains the following variables:

- `BOT_TOKEN`: The token for Silly Status.
- `NOTIFY_CHANNEL_ID`: The channel ID where notifications should be sent.
- `TARGET_BOT_ID`: The ID of the bot being monitored.
- `NOTIFY_USER_ID`: The user ID to notify when the bot goes offline.
- `BOT_GUILD`: The guild (server) ID where both bots are members.

## Contributions and Support

Your contributions are welcome! If you'd like to improve Silly Status or have any issues, please open an issue or submit a pull request on GitHub.

## License

Silly Status is released under the MIT License. See the LICENSE file for more details.