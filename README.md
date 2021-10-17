Very basic Python Status Bot for Discord. 

To edit status go into the main.py file and change where it says Status. 

---------------------------------------------
For Playing status: await client.change_presence(activity=discord.Game('#'))

For Streaming status: await client.change_presence(activity=discord.Streaming(name='#', url='#'))

For Listening status: await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='#'))

--------------------------------------------

Any issues contact 
rhys#9931 on discord!
