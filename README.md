# Toolpath-Generation
## Checklist
[image](https://user-images.githubusercontent.com/79973649/110300592-54208880-7ff7-11eb-9b82-80e1ff1f0fbc.png)


//Briefly describe what the model, and more importanly the Grashopper part does for the user
These files generate a single continuous toolpath from a 3D Voronoi structure with the aim of 3D printing.

## Prerequisites
- The scripts are made in Rhino 7 and Grasshopper
- Required Grasshopper Plugins:
  - Anemone
  - Pufferfish
  - Human
  - Kangaroo 0.0.9.9
  - EleFront
  - ShortestWalk.gh
  - Clipper

## Usage
The process consists of a sequence of scripts which need to be run and baked in this order:
- Toolpaths.gh
- Continuous Toolpaths.gh
- 
//The main geometry is in Toolpaths.3dm. After baking the curves in Toolpaths.gh the .3dm file becomes too large. We'll need to find a proper strategy for this.


An initial voronoi structure is provided. This geometry can be replaced with custom ones. The requirements of this geometry are:
- Cellular structure
- Generated considering printer requirements (max. overhang, level of printable detail etc.; also see: http://cs.roboticbuilding.eu/index.php/2021W3:Online)
- Geometry needs to be positioned with the Z-axis as the print direction
- Geometry needs to be split in print fragments if necessary to create a flat section to be positioned at the printing bed
- Cells are individual meshes
- Can contain closed as well as open cells
- Meshes describing the cells should be placed in the layer: Fragment::Voronoi Structure::Cells
- A bounding box (as a mesh) needs to be draw around the geometry in xyz orientation in layer: Fragment::Print Volume



## Layout
The scripts are organized according certain principles considering the layout. 

Every script start with a title and abstract:
![image](https://user-images.githubusercontent.com/79973649/110442889-9a3f2000-80bb-11eb-8a9f-126067af3967.png)
Make sure the file is saved on this view when the file is public.

The components are organized and ordered in groups and subgroups. Every group has at least a title. If required it also contains a description. The smallest groups are titled in the group header, a level above that by a scribble with font-size 25, and the main groups with a scribble of 50.
![image](https://user-images.githubusercontent.com/79973649/110443530-4f71d800-80bc-11eb-814d-444d47377813.png)

The descriptions are made in white panels.
![image](https://user-images.githubusercontent.com/79973649/110443719-8516c100-80bc-11eb-8f4e-a6d0db2a8e33.png)

Unresolved issues are appointed with red panels.
![image](https://user-images.githubusercontent.com/79973649/110444078-e8a0ee80-80bc-11eb-8e5d-b0ee60f26790.png)

Changes are visualized by colored groups. Red groups are the old groups which can be deleted, green ones are added and yellow groups have been edited. Add a panel in the relating color to describe the changes.
![image](https://user-images.githubusercontent.com/79973649/110445019-fc008980-80bd-11eb-8929-65c0a9571418.png)
![image](https://user-images.githubusercontent.com/79973649/110445135-1c304880-80be-11eb-9902-e7f920dd7066.png)
If the changes have been made in a (Github-)branch, add a readme to summarize all the changes.
