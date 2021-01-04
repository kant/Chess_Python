### CHESS GAME MADE BY JULIAN SEHBAOUI ###

#importing nessesary libaries and own classes from the components folder#
import pygame
import json
import os
from components.pieces_cls import Pieces
from components.pawns_cls import WhitePawns, BlackPawns
from components.bishops_cls import Bishops
from components.rooks_cls import Rooks
from components.knights_cls import Knights
from components.queens_cls import Queens
from components.kings_cls import Kings
from components.board_cls import Board

# resetting the variables in the .json file#
json_file = open(r'components\constants.json', 'r')
json_content = json.load(json_file)
json_content["round_int"] = 0
json_file.close()
json_file = open(r'components\constants.json', 'w')
json_file.writelines(json.dumps(json_content))
json_file.close()


def main():
    #initiating pygame#
    pygame.init()

    #reading the constants from the json file#
    json_file = open(os.getcwd()+r"\components\constants.json", "r")
    json_content = json.load(json_file)
    round_int = json_content["round_int"]
    tile_size = json_content["tile_size"]
    json_file.close()

    #setting up the variables for a new and fresh game#
    screen_size = (9*tile_size, 10*tile_size)
    go = True
    Pieces.white_is_checked = False
    Pieces.black_is_checked = False    

    #creating the surfaces#
    screen = pygame.display.set_mode(screen_size)
    s = pygame.Surface((8*tile_size, 8*tile_size))

    #window caption#
    pygame.display.set_caption("Chess")

    #creating a clock for the ingame ticks#
    clock = pygame.time.Clock()
    
    #creating the board on the subsurface#
    board = Board(master = s, width = 8, height = 8, tile_size = tile_size, color_a = (245, 216, 188), color_b = (176, 142, 109))
    board.draw_board()

    #loading and resizing the images for the pieces#
    white_pawn_img = pygame.image.load(r'assets/white_pawn.png')
    white_rook_img = pygame.image.load(r'assets/white_rook.png')
    white_knight_img = pygame.image.load(r'assets/white_knight.png')
    white_bishop_img = pygame.image.load(r'assets/white_bishop.png')
    white_queen_img = pygame.image.load(r'assets/white_queen.png')
    white_king_img = pygame.image.load(r'assets/white_king.png')
    black_pawn_img = pygame.image.load(r'assets/black_pawn.png')
    black_rook_img = pygame.image.load(r'assets/black_rook.png')
    black_knight_img = pygame.image.load(r'assets/black_knight.png')
    black_bishop_img = pygame.image.load(r'assets/black_bishop.png')
    black_queen_img = pygame.image.load(r'assets/black_queen.png')
    black_king_img = pygame.image.load(r'assets/black_king.png')

    white_pawn_img = pygame.transform.scale(white_pawn_img, (tile_size, tile_size))
    white_rook_img = pygame.transform.scale(white_rook_img, (tile_size, tile_size))
    white_knight_img = pygame.transform.scale(white_knight_img, (tile_size, tile_size))
    white_bishop_img = pygame.transform.scale(white_bishop_img, (tile_size, tile_size))
    white_queen_img = pygame.transform.scale(white_queen_img, (tile_size, tile_size))
    white_king_img = pygame.transform.scale(white_king_img, (tile_size, tile_size))
    black_pawn_img = pygame.transform.scale(black_pawn_img, (tile_size, tile_size))
    black_rook_img = pygame.transform.scale(black_rook_img, (tile_size, tile_size))
    black_knight_img = pygame.transform.scale(black_knight_img, (tile_size, tile_size))
    black_bishop_img = pygame.transform.scale(black_bishop_img, (tile_size, tile_size))
    black_queen_img = pygame.transform.scale(black_queen_img, (tile_size, tile_size))
    black_king_img = pygame.transform.scale(black_king_img, (tile_size, tile_size))


    #creating the pieces

    WhitePawns(master = s, name = 'A-Pawn-W', tile_x = 0, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'B-Pawn-W', tile_x = 1, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'C-Pawn-W', tile_x = 2, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'D-Pawn-W', tile_x = 3, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'E-Pawn-W', tile_x = 4, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'F-Pawn-W', tile_x = 5, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'G-Pawn-W', tile_x = 6, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    WhitePawns(master = s, name = 'H-Pawn-W', tile_x = 7, tile_y = 6, farbe = 'weiss', image = white_pawn_img)
    Rooks(master = s, name = 'L-Rook-W', tile_x = 0, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    Rooks(master = s, name = 'R-Rook-W', tile_x = 7, tile_y = 7, farbe = 'weiss', image = white_rook_img)
    Knights(master = s, name = 'L-Knight-W', tile_x = 6, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    Knights(master = s, name = 'R-Knight-W', tile_x = 1, tile_y = 7, farbe = 'weiss', image = white_knight_img)
    Bishops(master = s, name = 'L-Bishop-W', tile_x = 2, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    Bishops(master = s, name = 'R-Bishop-W', tile_x = 5, tile_y = 7, farbe = 'weiss', image = white_bishop_img)
    Queens(master = s, name = 'Queen-W', tile_x = 3, tile_y = 7, farbe = 'weiss', image = white_queen_img)
    Kings(master = s, name = 'King-W', tile_x = 4, tile_y = 7, farbe = 'weiss', image = white_king_img)
    BlackPawns(master = s, name = 'A-Pawn-B', tile_x = 0, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'B-Pawn-B', tile_x = 1, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'C-Pawn-B', tile_x = 2, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'D-Pawn-B', tile_x = 3, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'E-Pawn-B', tile_x = 4, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'F-Pawn-B', tile_x = 5, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'G-Pawn-B', tile_x = 6, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    BlackPawns(master = s, name = 'H-Pawn-B', tile_x = 7, tile_y = 1, farbe = 'schwarz', image = black_pawn_img)
    Rooks(master = s, name = 'L-Rook-B', tile_x = 0, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    Rooks(master = s, name = 'R-Rook-B', tile_x = 7, tile_y = 0, farbe = 'schwarz', image = black_rook_img)
    Knights(master = s, name = 'L-Knight-B', tile_x = 1, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    Knights(master = s, name = 'R-Knight-B', tile_x = 6, tile_y = 0, farbe = 'schwarz', image = black_knight_img)
    Bishops(master = s, name = 'L-Bishop-B', tile_x = 2, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    Bishops(master = s, name = 'R-Bishop-B', tile_x = 5, tile_y = 0, farbe = 'schwarz', image = black_bishop_img)
    Queens(master = s, name = 'Queen-B', tile_x = 3, tile_y = 0, farbe = 'schwarz', image = black_queen_img)
    Kings(master = s, name = 'King-B', tile_x = 4, tile_y = 0, farbe = 'schwarz', image = black_king_img)

    #a list for every possesed tile on the board#
    occupied_tiles = [] 

    #the mainloop#
    while go:

        #setting the framerate#
        clock.tick(60)

        #refreshing the occupied_tiles-list#
        occupied_tiles.clear()
        for piece in Pieces.all_pieces_list:
            occupied_tiles.append((piece.x, piece.y))

        #refreshing the round counter#
        json_file = open(os.getcwd()+r"\components\constants.json", "r")
        json_content = json.load(json_file)
        round_int = json_content["round_int"]
        json_file.close()

        #drawing the board#
        board.draw_board()

        #detecting if the white king is checked#
        if round_int % 2 == 1:
            for white_king in Pieces.all_pieces_list:
                if isinstance(white_king, Kings) and white_king.farbe == (255, 255, 255):
                    for piece in Pieces.all_pieces_list:
                        if piece != white_king and piece.farbe != white_king.farbe:
                            if (white_king.x, white_king.y) in piece.attacted_tiles():
                                Pieces.white_is_checked = True
                                Pieces.checking_piece = piece
                                break
                            else:
                                Pieces.white_is_checked = False

        #detecting if the balck king is checked#
        elif round_int % 2 == 0:
            for black_king in Pieces.all_pieces_list:
                if isinstance(black_king, Kings) and black_king.farbe == (0, 0, 0):
                    for piece in Pieces.all_pieces_list:
                        if piece != black_king and piece.farbe != black_king.farbe:
                            if (black_king.x, black_king.y) in piece.attacted_tiles():
                                Pieces.black_is_checked = True
                                Pieces.checking_piece = piece
                                break
                            else:
                                Pieces.black_is_checked = False

        #highlighting the checked king#
        if Pieces.white_is_checked:
            for king in Pieces.all_pieces_list:
                if isinstance(king, Kings) and king.farbe == (255,255,255):
                    board.check(king_pos = (king.x, king.y))

        #highlighting the checked king#            
        elif Pieces.black_is_checked:
            for king in Pieces.all_pieces_list:
                if isinstance(king, Kings) and king.farbe == (0,0,0):
                    board.check(king_pos = (king.x, king.y))

        #drawing all the pieces#
        for pieces in Pieces.all_pieces_list:
            pieces.draw(screen)
        
        #updating the mainsurface#
        pygame.display.update()

        #updating the subsurface#
        screen.blit(s, (0, 2*tile_size))

        #checking for events#
        for event in pygame.event.get():

            #closing the screen by clicking the X#
            if event.type == pygame.QUIT:
                go = False
 
            #Keyboard-Inputs#
            if event.type == pygame.KEYDOWN:

                #kill window if ESC is pressed#
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                
                #(TEMP) my information key (arrow down) to get certain information#
                if event.key == pygame.K_DOWN:
                    print(Pieces.black_is_checked)

            #left mouse click#
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #getting the mouseposition and than correcting it by the relative position of the subsurface#
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = (mouse_pos[0], mouse_pos[1]-2*tile_size)

                #checking if a Piece stands on the clicked tile#
                for piece in Pieces.all_pieces_list:
                    if mouse_pos[0] >= piece.x and mouse_pos[1] >=piece.y:
                        if mouse_pos[0] < piece.x+tile_size and mouse_pos[1] < piece.y+tile_size:
                            
                            #if the clicked piece is one of the team that currently is to move...#
                            if round_int % 2 == 1 and piece.farbe == (0,0,0) or round_int % 2 == 0 and piece.farbe == (255, 255, 255):

                                #...wait for the second mouse input#
                                piece.move(occupied_tiles = occupied_tiles, board = board, screen = screen)

                                #check if the white kiung is checked#
                                if round_int % 2 == 1:
                                    for white_king in Pieces.all_pieces_list:
                                        if isinstance(white_king, Kings) and white_king.farbe == (255, 255, 255):
                                            for piece in Pieces.all_pieces_list:
                                                if piece != white_king and piece.farbe != white_king.farbe:
                                                    if (white_king.x, white_king.y) in piece.attacted_tiles():
                                                        Pieces.white_is_checked = True
                                                        Pieces.checking_piece = piece
                                                        break
                                                    else:
                                                        Pieces.white_is_checked = False
                                #check if the white is checked#
                                elif round_int % 2 == 0:
                                    for black_king in Pieces.all_pieces_list:
                                        if isinstance(black_king, Kings) and black_king.farbe == (0, 0, 0):
                                            for piece in Pieces.all_pieces_list:
                                                if piece != black_king and piece.farbe != black_king.farbe:
                                                    if (black_king.x, black_king.y) in piece.attacted_tiles():
                                                        Pieces.black_is_checked = True
                                                        Pieces.checking_piece = piece
                                                        break
                                                    else:
                                                        Pieces.black_is_checked = False
        
    #resetting the variables in the .json file#
    json_file = open(r'components\constants.json', 'r')
    json_content = json.load(json_file)
    json_content["round_int"] = 0
    json_file.close()
    json_file = open(r'components\constants.json', 'w')
    json_file.writelines(json.dumps(json_content))
    json_file.close()


if __name__ == '__main__':
    main()

