# INSTAGRAM:  xyzrich.a
# DISCORD: @9li2
# VERSION BROADCAST ≥ 1
# Supp Server  :  discord.gg/freeservice


import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle, Embed, Interaction, ui

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

class BroadcastView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(label="ارسال الغير متصلين", style=ButtonStyle.danger)
    async def send_to_offline(self, button: ui.Button, interaction: Interaction):
        await interaction.response.send_message("Enter Your Message:", ephemeral=True)

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            message = await bot.wait_for("message", check=check, timeout=60)
            offline_members = [member for member in interaction.guild.members if member.status == nextcord.Status.offline]
            for member in offline_members:
                try:
                    await member.send(f"{member.mention}\n{message.content}")
                except:
                    continue
            await interaction.followup.send(f"Sent successfully to {len(offline_members)} offline members!", ephemeral=True)
        except:
            await interaction.followup.send("Timeout. No message sent.", ephemeral=True)

    @ui.button(label="ارسال لمتصلين", style=ButtonStyle.primary)
    async def send_to_online(self, button: ui.Button, interaction: Interaction):
        await interaction.response.send_message("Enter Your Message:", ephemeral=True)

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            message = await bot.wait_for("message", check=check, timeout=60)
            online_members = [member for member in interaction.guild.members if member.status != nextcord.Status.offline]
            for member in online_members:
                try:
                    await member.send(f"{member.mention}\n{message.content}")
                except:
                    continue
            await interaction.followup.send(f"Sent successfully to {len(online_members)} online members!", ephemeral=True)
        except:
            await interaction.followup.send("Timeout. No message sent.", ephemeral=True)

    @ui.button(label="ارسال للجميع", style=ButtonStyle.success)
    async def send_to_all(self, button: ui.Button, interaction: Interaction):
        await interaction.response.send_message("Enter Your Message:", ephemeral=True)

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            message = await bot.wait_for("message", check=check, timeout=60)
            all_members = interaction.guild.members
            for member in all_members:
                try:
                    await member.send(f"{member.mention}\n{message.content}")
                except:
                    continue
            await interaction.followup.send(f"Sent successfully to {len(all_members)} members!", ephemeral=True)
        except:
            await interaction.followup.send("Timeout. No message sent.", ephemeral=True)

@bot.command()
async def start(ctx, *, title):
    # تحديد الـ ID المسموح له باستخدام الأمر
    allowed_user_id = 123456789012345678  # استبدل هذا بالـ ID المطلوب
    if ctx.author.id != allowed_user_id:
        await ctx.send("ليس لديك الإذن لاستخدام هذا الأمر.")
        return

    embed = Embed(title=title, description="اضغط على الازرار الاسفل لإرسال البرودكاست", color=0x00ff00)
    view = BroadcastView()
    await ctx.send(embed=embed, view=view)

bot.run("")
