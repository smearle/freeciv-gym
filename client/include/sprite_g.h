/********************************************************************** 
 Freeciv - Copyright (C) 1996-2005 - Freeciv Development Team
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
***********************************************************************/
#ifndef FC__SPRITE_G_H
#define FC__SPRITE_G_H

struct Sprite;			/* opaque type, real type is gui-dep */

const char **gfx_fileextensions(void);

struct Sprite *load_gfxfile(const char *filename);
struct Sprite *crop_sprite(struct Sprite *source,
			   int x, int y, int width, int height,
			   struct Sprite *mask,
			   int mask_offset_x, int mask_offset_y);
void get_sprite_dimensions(struct Sprite *sprite, int *width, int *height);
void free_sprite(struct Sprite *s);

#endif  /* FC__SPRITE_G_H */
