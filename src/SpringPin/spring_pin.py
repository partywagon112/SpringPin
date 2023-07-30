import pcbnew
import wx
import os
import pandas

# https://docs.wxpython.org/wx.FileDialog.html
# https://jeffmcbride.net/kicad-track-layout/


class MoveComponentsCSV(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Define Component Locations from CSV."
        self.category = "Modify PCB"
        self.description = "Used to update the centre of components - useful for defining the locations of test points \
            and spring pins."
        self.show_toolbar_button = False
        # self.icon_file_name = os.path.join(os.path.dirname(__file__))
    
    def Run(self):
        self.board: pcbnew.BOARD = pcbnew.GetBoard()

        filepath = self.__get_filepath()
        if filepath is None:
            return
        
        positions = self.__get_list_from_table(filepath)

        # stick everything together
        group: pcbnew.PCB_GROUP = pcbnew.PCB_GROUP(self.board)
        self.board.Add(group)

        # arrange the items 
        for position in positions:
            footprint:pcbnew.FOOTPRINT = self.board.FindFootprintByReference(position['designator'])
            # use early return if the footprint is empty.
            if footprint == None:
                continue
            footprint.SetPosition(pcbnew.VECTOR2I_MM(position['x'], position['y']))
            
            # add all the items to one collective.
            group.AddItem([])

    def __get_filepath(self) -> str:
        with wx.FileDialog(
            wx.GetActiveWindow(), 
            "Open table defining location data.", 
            wildcard="CSV Files (*.csv)|*.csv", 
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:

            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return None
            
            return str(file_dialog.GetPath())
    
    def __get_list_from_table(self, filepath):
        """
        The filepath must be checked before it goes in!
        """
        import_dataframe: pandas.DataFrame = pandas.read_csv(filepath, header=0)
        if list(import_dataframe.keys()) != ['designator', 'x', 'y']:
            raise ValueError("Incorrect key arrangement in CSV. Use \'designator\', \'x\', \'y\' as the headings in the first row\
                and define components to shift accordingly.")
 
        return import_dataframe.to_dict(orient='records')

    def confirm(self):
        confirmation_dialog = wx.MessageDialog(
            wx.GetActiveWindow(),
            f"Confirm to move all components?",
            f"Continue?",
            wx.YES_NO | wx.CANCEL
        )

        if confirmation_dialog.ShowModal() == wx.ID_YES:
            return True
        else:
            return False