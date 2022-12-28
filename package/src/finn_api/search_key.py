class SearchKey:
    """
    Base class for search keys
    """

class realestate(SearchKey):
    homes = "SEARCH_ID_REALESTATE_HOMES"
    lettings = "SEARCH_ID_REALESTATE_LETTINGS"
    newbuildings = "SEARCH_ID_REALESTATE_NEWBUILDINGS"
    plots = "SEARCH_ID_REALESTATE_PLOTS"
    leisure = "SEARCH_ID_REALESTATE_LEISURE_SALE"
    leisure_plots = "SEARCH_ID_REALESTATE_LEISURE_PLOTS"
    commercial = "SEARCH_ID_COMMERCIAL_SALE"
    commercial_rent = "SEARCH_ID_COMMERCIAL_RENT"
    commercial_plots = "SEARCH_ID_COMMERCIAL_PLOTS"
    company = "SEARCH_ID_COMPANY_SALE"

class mc(SearchKey):
    used = "SEARCH_ID_MC_USED"
    scooter = "SEARCH_ID_MC_SCOOTER"
    snowmobile = "SEARCH_ID_MC_SNOWMOBILE"
    atv = "SEARCH_ID_MC_ATV"


class car(SearchKey):
    used = "SEARCH_ID_CAR_USED"
    imports = "SEARCH_ID_CAR_PARALLEL_IMPORT"
    mobile_home = "SEARCH_ID_CAR_MOBILE_HOME"
    caravan = "SEARCH_ID_CAR_CARAVAN"
    car_van = "SEARCH_ID_CAR_VAN"

class b2b(SearchKey):
    truck = "SEARCH_ID_CAR_TRUCK"
    bus = "SEARCH_ID_CAR_BUS"
    agriculture = "SEARCH_ID_CAR_AGRI"
    tractor = "SEARCH_ID_AGRICULTURE_TRACTOR"
    threshing = "SEARCH_ID_AGRICULTURE_THRESHING"
    agriculture_tool = "SEARCH_ID_AGRICULTURE_TOOL"

class boat(SearchKey):
    used = "SEARCH_ID_BOAT_USED"
    used_wanted = "SEARCH_ID_BOAT_USED_WANTED"
    rent = "SEARCH_ID_BOAT_RENT"
    motor = "SEARCH_ID_BOAT_MOTOR"
    motor_parts = "SEARCH_ID_BOAT_MOTOR_PARTS"
    motor_parts_wanted = "SEARCH_ID_BOAT_PARTS_MOTOR_WANTED"
    dock = "SEARCH_ID_BOAT_DOCK"
    dock_wanted = "SEARCH_ID_BOAT_DOCK_WANTED"


class bap(SearchKey):
    common = "SEARCH_ID_BAP_COMMON"