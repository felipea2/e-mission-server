import logging
import emission.core.wrapper.wrapperbase as ecwb

class Stop(ecwb.WrapperBase):
    props = {"user_id": ecwb.WrapperBase.Access.WORM, # start UTC timestamp (in secs)
             "trip_id": ecwb.WrapperBase.Access.WORM, # trip_id of the parent trip
             "enter_ts": ecwb.WrapperBase.Access.WORM,  # the timestamp of entry (in secs)
             "enter_fmt_time": ecwb.WrapperBase.Access.WORM, # formatted entry time in timezone of place
             "exit_ts": ecwb.WrapperBase.Access.WORM,        # the timestamp of exit (in secs)
             "exit_fmt_time": ecwb.WrapperBase.Access.WORM,  # formatted time in timezone of place
             "ending_section": ecwb.WrapperBase.Access.WORM,  # the id of the trip just before this
             "starting_section": ecwb.WrapperBase.Access.WORM,  # the id of the trip just after this
             "location": ecwb.WrapperBase.Access.WORM, # the location in geojson format
             "source": ecwb.WrapperBase.Access.WORM,   # the method used to generate this place
             "duration": ecwb.WrapperBase.Access.WORM}    # the duration for which we were in this place

    enums = {}
    geojson = ["location"]
    nullable = ["enter_ts", "enter_fmt_time", "ending_section", # for the start of a chain
                "exit_ts", "exit_fmt_time", "starting_section"] # for the end of a chain

    def _populateDependencies(self):
        pass
