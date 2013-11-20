import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def clearSomeSpace(x, y, z):
            mc.setBlocks(x - 10, y, z - 20, x + 10, y + 20, z + 20, block.AIR)

def addWindow(x, y, z, width, height, depth):
            if width == 1 and height == 1 and depth == 1:
                        mc.setBlock(x, y, z, block.GLASS)
            else:
                        mc.setBlocks(x, y, z, x + width - 1, y + height - 1, z + depth - 1, block.GLASS)

def addDoor(x, y, z):
            mc.setBlock(x, y, z, block.DOOR_WOOD)
            mc.setBlock(x, y + 1, z, block.DOOR_WOOD)
            mc.setBlock(x, y + 2, z, block.DOOR_WOOD)
            mc.setBlock(x - 1, y, z, block.DOOR_WOOD)
            mc.setBlock(x - 1, y + 1, z, block.DOOR_WOOD)
            mc.setBlock(x - 1, y + 2, z, block.DOOR_WOOD)

def addBed(x, y, z):
            mc.setBlock(x, y, z, block.BED)
            mc.setBlock(x, y, z + 1, block.BED, 255)

def addTeleport(x, y, z):
            mc.setBlocks(x + 7, y + 4, z + 11, x + 8, y + 4, z + 12, block.GOLD_BLOCK)
            mc.setBlocks(x - 1, y + 15, z - 23, x + 2, y + 15, z - 26, block.GLOWSTONE_BLOCK)
            mc.setBlocks(x, y + 15, z - 25, x + 1, y + 15, z - 24, block.GOLD_BLOCK)

def isOnHouseTeleport(x, y, z, hx, hy, hz):
            return x >= hx + 7 and x <= hx + 8 and y == hy + 5 and z >= hz + 11 and z <= hz + 12

def isOnSkyTeleport(x, y, z, hx, hy, hz):
            return x >= hx and x <= hx + 1 and y == hy + 16 and z >= hz - 25 and z <= hz - 24

def teleportFromHouse(x, y, z):
            mc.postToChat("Teleporting....")
            mc.player.setTilePos(x, y + 20, z - 23)

def teleportFromSky(x, y, z):
            mc.postToChat("Teleporting....")
            mc.player.setTilePos(x + 6, y + 6, z + 11)

position = mc.player.getTilePos()

houseX = position.x + 3
houseY = position.y
houseZ = position.z

houseWidth = 10
houseHeight = 8
houseLength = 15

clearSomeSpace(houseX, houseY, houseZ)

# Create the house
mc.setBlocks(houseX, houseY, houseZ, houseX + houseWidth, houseY + houseHeight, houseZ + houseLength, block.TNT )

# Hollow it out with air
mc.setBlocks(houseX + 1, houseY + 1, houseZ + 1, houseX + (houseWidth - 1), houseY + (houseHeight - 1), houseZ + (houseLength - 1), block.AIR)

# Door
addDoor(houseX + houseWidth / 2, houseY, houseZ)

# Windows
addWindow(houseX + 1, houseY + 2, houseZ, 1, 1,1 )
addWindow(houseX + 8, houseY + 2, houseZ, 1, 1,1 )
addWindow(houseX + 1, houseY + 6, houseZ, 1, 1,1 )
addWindow(houseX + 8, houseY + 6, houseZ, 1, 1,1 )
addWindow(houseX + 10, houseY + 2, houseZ + 2, 1, 5, 6)

# Add a load of diamond blocks on top of the house!
for i in range(5, 25):
            mc.setBlock (houseX + i, houseY + houseHeight + 1, houseZ + 5, block.DIAMOND_BLOCK)
            i = i + 1

# Add some TNT on the ground floor
mc.setBlock(houseX + 5, houseY + 1, houseZ + 4, block.TNT)
mc.setBlock(houseX + 5, houseY + 2, houseZ + 4, block.LAVA)

# Add a second floor
mc.setBlocks(houseX + 1, houseY + 4, houseZ + 1, houseX + (houseWidth - 1), houseY + 4, houseZ + (houseLength - 1), block.WOOD)

# Put a bed upstairs
addBed(houseX + 2, houseY + 5, houseZ + 7)

# Make the floor wooden
mc.setBlocks(houseX + 1, houseY, houseZ + 1, houseX + (houseWidth - 1), houseY, houseZ + (houseLength - 1), block.WOOD)

# Stairs to 2nd floor and make a hole in the ceiling to go through
mc.setBlock(houseX + 3, houseY + 1, houseZ + 5, block.STAIRS_WOOD)
mc.setBlock(houseX + 4, houseY + 2, houseZ + 5, block.STAIRS_WOOD)
mc.setBlock(houseX + 5, houseY + 3, houseZ + 5, block.STAIRS_WOOD)
mc.setBlocks(houseX + 3, houseY + 4, houseZ + 5, houseX + 5, houseY + 4, houseZ + 5, block.AIR)

# Add some light to downstairs
mc.setBlock(houseX + 5, houseY + 1, houseZ + 9, block.FIRE, 255)
mc.setBlock(houseX + 2, houseY + 1, houseZ + 2, block.FIRE, 255)
mc.setBlock(houseX + 8, houseY + 1, houseZ + 5, block.FIRE, 255)

# And upstairs
mc.setBlock(houseX + 5, houseY + 5, houseZ + 9, block.FIRE, 255)
mc.setBlock(houseX + 2, houseY + 5, houseZ + 2, block.FIRE, 255)
mc.setBlock(houseX + 8, houseY + 5, houseZ + 5, block.FIRE, 255)

# Add a teleport
addTeleport(houseX, houseY, houseZ)

while(True):
            playerX, playerY, playerZ = mc.player.getTilePos()
            if isOnHouseTeleport(playerX, playerY, playerZ, houseX, houseY, houseZ):
                        teleportFromHouse(houseX, houseY, houseZ)
            elif isOnSkyTeleport(playerX, playerY, playerZ, houseX, houseY, houseZ):
                        teleportFromSky(houseX, houseY, houseZ)
                        
            time.sleep(1)
