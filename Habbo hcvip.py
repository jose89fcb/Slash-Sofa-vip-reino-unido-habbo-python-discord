import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext

with open("configuracion.json") as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="sofahc", description="Keko habbo Hotel",
    options=[
                create_option(
                  name="keko1",
                  description="Escribe el keko 1",
                  option_type=3,
                  required=True
                ),
                 create_option(
                  name="keko2",
                  description="Escribe el keko 2",
                  option_type=3,
                  required=True,
                  
                  
                
               
                  
                )
             ])


async def _sofahc(ctx:SlashContext, keko1:str,keko2:str):
    await ctx.defer()
   
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko1}")
    response1 = requests.get(f"https://www.habbo.es/api/public/users?name={keko2}")
    
    try:

     habbo = response.json()['figureString']
    except KeyError:
        habbo="Keko 1 no existe ❌"

    try:

     habbo1 = response1.json()['figureString']
    except KeyError:
      habbo1="keko 2 no existe ❌"

   
    

    
    


    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+habbo+"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
   
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    url1 = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo1 +"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
    habbol = Image.open(io.BytesIO(requests.get(url1).content))
    habbol = habbol.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 2
    
    
    img2 = img1.copy()
    
    trozoSOFAHC = Image.open(r"imagenes/TrozoHCSofa.png").convert("RGBA")
    img1 = trozoSOFAHC.resize((200,135), Image.Resampling.LANCZOS)#tamaño del trozo de sofa
    
    img1 = Image.open(r"imagenes/HCSofa.png").convert("RGBA") #Imagen del sofa habbo club
    img1 = img1.resize((200,135), Image.Resampling.LANCZOS)


    

    
    

    img1.paste(img2,(10,0), mask = img2) #Posicion del keko 1
    
    ###
    

    img1.paste(habbol,(40,10), mask = habbol) #Posicion del keko 2

    img1.paste(trozoSOFAHC,(0,0), mask = trozoSOFAHC) #Posicion del trozo de sofa
    
  
   
    
    
   


    
    
    
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))

       




      
    
    
         

         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])    


