#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:26:21 2018

@author: skaering
"""

organs = ["sheath", "cast cuticle", "cuticle", "exocuticle", "layers", "cuticle layers",
          "v-shaped mark", "annuli", "striae", "cuticular annulations", "annules",
          "posterior edge ornementations", "head annuli", "anterior end annuli",
          "cephalic region annuli", "labial region annuli", "lip annuli",
          "longitudinal striae", "longitudinal striae on head annuli",
          "horizntal lines on the annuli of the anterior end", "longitudinal grooves",
          "longitudinal grooves on head area", "radial grooves", "head basal annulus",
          "longitudinal striae on basal anulus", "labial disc", "oral disc",
          "circumoral ridge", "head disc", "first annulus", "sectors", "collar",
          "head annuli", "labial pattern", "lip pattern", "labial disc", "oral disc",
          "circumoral ridge", "head disc", "first labial annulus", "first lip annulus",
          "first cephalic annulus", "lips", "sectors", "labial annulus sectors",
          "first annulus sectors", "sub-median sectors", "sub-median pseudolips",
          "sub-median liplets", "sub-median lobes", "neck annuli", "tail annuli",
          "fused portion", "tail end annuli", "striae at terminus", "lateral field",
          "lateral alae", "wings", "lines", "lateral field lines", "incisures", "involutions",
          "section with", "junction", "section with x lines", "section with y lines",
          "bands", "lateral field bands", "areolations", "cross striations",
          "body annuli extending in lateral field", "lateral field crossed by body annuli",
          "annulation continues across the lateral field", "lateral field", "anastomoses",
          "subcuticular markings", "punctations", "hypodermis", "thorneian cells",
          "stomodeum", "stoma", "buccal cavity", "oral opening", "prostoma", "mouth opening",
          "vestibule", "guiding apparatus", "stylet guide", "spear guiding", "apparatus",
          "anterior part", "anterior part of the vestibule", "skeletal tube", "posterior part",
          "posterior part of the vestibule", "stylet", "spear", "stomatostyle", "base",
          "stylet base", "stylet lumen", "cone", "conus", "apex", "prorhabdions",
          "metenchium", "conical part of stylet", "tapering fore part", "stylet cone",
          "anterior part of stylet", "shaft", "cylindrus", "cylindrical part of the stylet",
          "telenchium", "knobs", "stylet knobs", "anterior face of knobs",
          "anterior part of knobs", "teeth", "anterior", "projections", "stylet knob teeth",
          "posterior face of knobs", "posterior part of knobs", "muscles", "stylet muscles",
          "protractors", "stylet protractors", "head musculature", "end", "end of stomodeum",
          "end of vestibule", "oesophagus", "pharynx", "lumen", "oesophageal lumen", "corpus",
          "procorpus", "precorpus", "junction procorpus median bulb",
          "junction between medial bulb et procorpus", "junction between procorpus and median bulb",
          "median bulb", "metacorpus", "metacorpal bulb", "post corpus", "valve",
          "median bulb valve", "pump", "valvular apparatus", "vesicles", "vesicles in median bulb",
          "grouping median bulb and isthmus", "junction median bulb and isthmus",
          "end of median bulb", "isthmus", "stem", "oesophageal glands", "oesophageal lobes",
          "glandular bulb", "gland bulb", "dorsal oesophageal gland", "dorsal gland opening",
          "nucleus", "dorsal gland nucleus", "subventral oesophageal glands",
          "subventral glands openings", "subventral gland nuclei",
          "oesophageal glands end", "gland overlap end", "cardia", "oesophago-intestinal junction",
          "oesophago-intestinal valve", "intestine", "mesenteron", "midgut", "lumen",
          "intestinal lumen", "fasciculi", "lateral canals", "serpentine", "origin",
          "origin of fasciculi", "fasciculi end", "proctodeum", "posterior gut",
          "hind gut", "sphincter muscle", "rectum", "wall", "rectum wall", "rectum glands",
          "rectal glands", "anus", "cloaca", "anal opening"]

properties = ["presence", "kind", "number", "thickness","number = R", "visibility", "size",
              "orientation", "shape", "width", "aspect", "arrangement", "number per number",
              "symmetry", "position relative to", "height", "diameter", "length",
              "size relative to", "appearance", "ratio", "distance to",
              "type", "location relative to", "texture", "Shape (type of stylet)",
              "posture", "angle to", "orientaion relative to", "position within",
              "angle with", "position", "habitus = posture = attitude", "angle",
              "color = colour", "diameter = width", "length relative to",
              "physiology", "position on", "Length (width)", "Width (=height)","depth"]

dimensionalProperties= ["width","diameter = width","Length (width)","Width (=height)","number = R","size", "number", "ratio","height", "diameter","depth"]
relativeProperties= ["position relative to", "orientaion relative to", "distance to", "angle with" , "angle to" , "length relative to"]
#source = "Female: Body usually in spiral shape.Lip region hemispherical, 4 or 5 often indistinct annules.Spear knobs with indented anterior surfaces. Excretory pore at level of anterior end of oesophageal glands. Hemizonid just anterior to excretory pore. Hemizonion usually not visible. Spermatheca usually conspicuous,offset without sperm. Phasmids 5 to 11 annules anterior to level of anus. Tail more curved dorsally, usually with slight ventral projection, 6 to 12 annules."
source= "tail end annuli position relative to lumen ";