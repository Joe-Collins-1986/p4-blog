from .models import Country, Visit

# albania = Country.objects.get(name='Albania')
# belgium = Country.objects.get(name='Belgium')
# bulgaria = Country.objects.get(name='Bulgaria')
# bosnia_herzegovina = Country.objects.get(name='Bosnia and Herzegovina')
# belarus = Country.objects.get(name='Belarus')
# switzerland = Country.objects.get(name='Switzerland')
# czech_republic = Country.objects.get(name='Czech Republic')
# germany = Country.objects.get(name='Germany')
# denmark = Country.objects.get(name='Denmark')
# estonia = Country.objects.get(name='Estonia')
# finland = Country.objects.get(name='Finland')
# united_kingdom = Country.objects.get(name='United Kingdom')
# greece = Country.objects.get(name='Greece')
# croatia = Country.objects.get(name='Croatia')
# hungary = Country.objects.get(name='Hungary')
# ireland = Country.objects.get(name='Ireland')
# iceland = Country.objects.get(name='Iceland')
# italy = Country.objects.get(name='Italy')
# lithuania = Country.objects.get(name='Lithuania')
# luxembourg = Country.objects.get(name='Luxembourg')
# latvia = Country.objects.get(name='Latvia')

# moldova = Country.objects.get(name='Moldova')
# montenegro = Country.objects.get(name='Montenegro')
# norway = Country.objects.get(name='Norway')
# poland = Country.objects.get(name='Poland')
# romania = Country.objects.get(name='Romania')
# serbia = Country.objects.get(name='Serbia')
# slovakia = Country.objects.get(name='Slovakia')
# slovenia = Country.objects.get(name='Slovenia')
# sweden = Country.objects.get(name='Sweden')
# ukraine = Country.objects.get(name='Ukraine')
# netherlands = Country.objects.get(name='Netherlands')
# portugal = Country.objects.get(name='Portugal')
# russia = Country.objects.get(name='Russian Federation')
# spain = Country.objects.get(name='Spain')
# france = Country.objects.get(name='France')
# malta = Country.objects.get(name='Malta')
# st_eustatius = Country.objects.get(name='St Eustatius')
# saba = Country.objects.get(name='Saba')
# canary_islands = Country.objects.get(name='Canary Islands')



        # if Albania.country_map.filter(user=request.user.id).exists():
        #     Albania_status = Albania.country_map.get(user=request.user.id)
        # else:
        #     Albania_status = 'not_visited'

        # if Belgium.country_map.filter(user=request.user.id).exists():
        #     Belgium_status = Belgium.country_map.get(user=request.user.id)
        # else:
        #     Belgium_status = 'not_visited'

        # if bulgaria.country_map.filter(user=request.user.id).exists():
        #     bulgaria_status = bulgaria.country_map.get(user=request.user.id)
        # else:
        #     bulgaria_status = 'not_visited'




        # country_list = ["albania", "belgium", "bulgaria", "bosnia_and_herzegovina", "belarus", "switzerland", "czech_republic",
        #                 "germany", "denmark", "estonia", "finland", "united_kingdom", "greece", "croatia", "hungary", "ireland",
        #                 "iceland", "italy", "lithuania", "luxembourg", "latvia", "moldova", "montenegro", "norway", "poland", "romania",
        #                 "serbia", "slovakia", "slovenia", "sweden", "ukraine", "netherlands", "portugal", "spain", "france",
        #                 "malta", "canary_islands"]


        # country_code_list = ['AL', 'BY', 'BE', 'BA', 'BG', 'HR', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IS',
        #                      'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'MD', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SK',
        #                      'SI', 'ES', 'SE', 'CH', 'UA', 'GB']



# .......................................
#         country_list = ["albania", "belgium", "bulgaria", "bosnia_and_herzegovina", "belarus", "switzerland", "czech_republic",
#                         "germany", "denmark", "estonia", "finland", "united_kingdom", "greece", "croatia", "hungary", "ireland",
#                         "iceland", "italy", "lithuania", "luxembourg", "latvia", "moldova", "montenegro", "norway", "poland", "romania",
#                         "serbia", "slovakia", "slovenia", "sweden", "ukraine", "netherlands", "portugal", "spain", "france",
#                         "malta", "canary_islands"]


#         dict = {}
#         for country in country_list:
#             key = country
#             dict[key] = Country.objects.get(slug=country)

#             status_dict = {}
#             if dict[key].country_map.filter(user=request.user.id).exists():
#                 key = f"{country}_status"
#                 status_dict[key] = dict[country].country_map.get(user=request.user.id)
#             else:
#                 key = f"{country}_status"
#                 status_dict[key] = "not_visited"

#             dict.update(status_dict) 
            
#         return render(request, "map/home.html", dict)





................__annotations__

<style>
    .visited {
      fill: rgb(70, 153, 11)
    }
    .not_visited {
      fill: rgb(171, 192, 11)
    }
    .wish_list {
      fill: rgb(105, 100, 56)
    }
</style>


<div>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      baseprofile="tiny"
      stroke-linecap="round"
      stroke-linejoin="round"
      version="1.2"
      viewbox="800 0 500 857"
    >
    <a class="{{ AL_status }}" href="{% url 'country' AL.id %}">
        <path
            d="M1088 228l0.4 1.2 1.4-0.6 1.2 1.7 1.3 0.7 0.6 2.3-0.5 2.2 1 2.7 2.3 1.5 0.1 1.7-1.7 0.9-0.1 2.1-2.2 3.1-0.9-0.4-0.2-1.4-3.1-2.2-0.7-3 0.1-4.4 0.5-1.9-0.9-1-0.5-2.1 1.9-3.1z"
            id="AL"
            name="Albania"
        ></path>
    </a>
    <a class="{{ belgium_status }}" href="{% url 'country' belgium.id %}">
        <path
            d="M1016.5 177.1l-0.4 4.2-1.3 0.2-0.4 3.5-4.4-2.9-2.5 0.5-3.5-2.9-2.4-2.5-2.2-0.1-0.8-2.2 3.9-1.2 3.6 0.5 4.5-1.3 3.1 2.7 2.8 1.5z"
            id="BE"
            name="Belgium"
    ></path>
    </a>
    <a class="{{ bulgaria_status }}" href="{% url 'country' bulgaria.id %}">
        <path
            d="M1132.6 221.6l-2.3 2.6-1.3 4.5 2.1 3.6-4.6-0.8-5 2 0.3 3.2-4.6 0.6-3.9-2.3-4 1.8-3.8-0.2-0.8-4.2-2.8-2.1 0.7-0.8-0.6-0.8 0.6-2 1.8-2-2.8-2.7-0.7-2.4 1.1-1.4 1.8 2.6 1.9-0.4 4 0.9 7.6 0.4 2.3-1.6 5.9-1.5 4 2.3 3.1 0.7z"
            id="BG"
            name="Bulgaria"
        ></path>
    </a>
    <a class="{{ bosnia_and_herzegovina_status }}" href="{% url 'country' bosnia_and_herzegovina.id %}">
        <path
            d="M1083 214.3l1.9-0.1-1.1 2.8 2.7 2.5-0.5 2.9-1.1 0.3-0.9 0.6-1.6 1.5-0.4 3.5-4.8-2.4-2.1-2.7-2.1-1.4-2.5-2.4-1.3-1.9-2.7-3 0.8-2.6 2 1.5 1-1.4 2.3-0.1 4.5 1.1 3.5-0.1 2.4 1.4z"
            id="BA"
            name="Bosnia and Herzegovina"
        ></path>
    </a>
    <a class="{{ belarus_status }}" href="{% url 'country' belarus.id %}">
        <path
            d="M1141.6 162.7l-3.9-0.2-0.8 0.6 1.5 2 2 4-4.1 0.3-1.3 1.4 0.3 3.1-2.1-0.6-4.3 0.3-1.5-1.5-1.7 1.1-1.9-0.9-3.9-0.1-5.7-1.5-4.9-0.5-3.8 0.2-2.4 1.6-2.3 0.3-0.5-2.8-1.9-2.8 2.8-1.3-0.4-2.4-1.7-2.3-0.6-2.7 4.7 0 4.8-2.3 0.5-3.4 3.6-2-1-2.7 2.7-1 4.6-2.3 5.3 1.5 0.9 1.5 2.4-0.7 4.8 1.4 1.1 2.9-0.7 1.6 3.8 4 2.1 1.1 0 1.1 3.4 1.1 1.7 1.6-1.6 1.3z"
            id="BY"
            name="Belarus"
        ></path>
    </a>
    <a class="{{ switzerland_status }}" href="{% url 'country' switzerland.id %}">
        <path
            d="M1034.4 197.5l0.2 1.1-0.7 1.5 2.3 1.2 2.6 0.2-0.3 2.5-2.1 1.1-3.8-0.8-1 2.5-2.4 0.2-0.9-1-2.7 2.2-2.5 0.3-2.2-1.4-1.8-2.7-2.4 1 0-2.9 3.6-3.5-0.2-1.6 2.3 0.6 1.3-1.1 4.2 0 1-1.3 5.5 1.9z"
            id="CH"
            name="Switzerland"
        ></path>
    </a>
    <a class="{{ czech_republic_status }}" href="{% url 'country' czech_republic.id %}">
        <path
            d="M1059.7 175.2l2.5 2 3.7 0.5-0.2 1.7 2.8 1.3 0.6-1.6 3.4 0.7 0.7 2 3.7 0.3 2.6 3.1-1.5 0-0.7 1.1-1.1 0.3-0.2 1.4-0.9 0.3-0.1 0.6-1.6 0.6-2.2-0.1-0.6 1.4-2.4-1.2-2.3 0.3-4-1.9-1.7 0.5-2.6 2.6-3.8-2.1-3-2.6-2.6-1.5-0.7-2.7-1-1.8 3.4-1.3 1.7-1.6 3.5-1.2 1.1-1.2 1.3 0.7 2.2-0.6z"
            id="CZ"
            name="Czech Republic"
        ></path>
    </a>
    <a class="{{ germany_status }}" href="{% url 'country' germany.id %}">
        <path
            d="M1053.9 158.9l1.4 3.1-1.2 1.7 1.9 2.1 1.5 3.3-0.2 2.2 2.4 3.9-2.2 0.6-1.3-0.7-1.1 1.2-3.5 1.2-1.7 1.6-3.4 1.3 1 1.8 0.7 2.7 2.6 1.5 3 2.6-1.6 2.9-1.7 0.8 1 4.1-0.4 1.1-1.7-1.3-2.4-0.2-3.5 1.1-4.4-0.3-0.6 1.7-2.7-1.7-1.4 0.3-5.5-1.9-1 1.3-4.2 0 0.4-4.5 2.4-4.2-7.2-1.2-2.4-1.6 0.2-2.7-1-1.4 0.4-4.2-1.1-6.5 2.9 0 1.2-2.3 0.9-5.6-0.9-2.1 0.8-1.3 4-0.3 1 1.3 3.1-3-1.3-2.3-0.4-3.4 3.7 0.8 2.9-0.9 0.3 2.3 4.9 1.4 0.1 2.2 4.7-1.2 2.6-1.6 5.6 2.4 2.4 1.9z"
            id="DE"
            name="Germany"
        ></path>
    </a>
    <a class="{{ denmark_status }}" href="{% url 'country' denmark.id %}">
        <path
            class="Denmark"
            d="M 1046.1 147.7 1043.7 152.6 1038.5 149.1 1037.6 146.6 1044.4 144.6 1046.1 147.7 Z"
        ></path>
    </a>
    <a class="{{ denmark_status }}" href="{% url 'country' denmark.id %}">
        <path
            class="Denmark"
            d="M 1033.3 151.5 1030.4 152.4 1026.7 151.6 1024.6 148.2 1024.2 142.1 1024.8 140.4 1026.1 138.6 1030.1 138.3 1031.7 136.6 1035.3 134.9 1035.3 138 1034.1 140 1034.8 141.6 1037.4 142.5 1036.4 144.8 1035 144.2 1031.9 148.5 1033.3 151.5 Z"
        ></path>
    </a>
    <a class="{{ estonia_status }}" href="{% url 'country' estonia.id %}">
        <path
            d="M1113.7 124.6l0.9 1-2.6 3.4 2.4 5.6-1.6 1.9-3.8-0.1-4.4-2.2-2.1-0.7-3.8 1-0.1-3.5-1.5 0.8-3.3-2.1-1-3.4 5.5-1.7 5.6-0.8 5.1 0.9 4.7-0.1z"
            id="EE"
            name="Estonia"
        ></path>
    </a>
    <a class="{{ finland_status }}" href="{% url 'country' finland.id %}">
        <path
            d="M1104.1 70.1l0.4 3.8 7.3 3.7-2.9 4.2 6.5 6.3-1.7 4.8 4.9 4.2-0.9 3.8 7.4 3.9-0.9 2.9-3.4 3.4-8 7.4-8 0.5-7.6 2.1-7.1 1.3-3.2-3.2-4.7-1.9 0.1-5.8-3-5.2 1.6-3.4 3.3-3.5 8.8-6.2 2.6-1.2-0.9-2.4-6.5-2.6-1.8-2.2-1.8-8.5-7.2-3.7-6-2.7 2.2-1.4 5.1 2.8 5.3-0.2 4.7 1.3 3.4-2.4 1.1-4 5.9-1.8 5.8 2.1-0.8 3.8z"
            id="FI"
            name="Finland"
        ></path>
    </a>
    <a class="{{ united_kingdom_status }}" href="{% url 'country' united_kingdom.id %}">
        <path
            class="United Kingdom"
            d="M 956.7 158.2 953.2 157 950.2 157.1 951.4 153.8 950.5 150.6 954.5 150.3 959.4 154.1 956.7 158.2 Z"
        ></path>
    </a>
    <a class="{{ united_kingdom_status }}" href="{% url 'country' united_kingdom.id %}">
        <path
            class="United Kingdom"
            d="M 972.6 129.5 967.5 136 972.2 135.2 977.3 135.2 976 140.1 971.7 145.5 976.6 145.8 976.9 146.5 981.1 153.6 984.3 154.6 987.2 161.6 988.6 164 994.5 165.1 993.9 169.1 991.5 170.9 993.4 174.1 989 177.3 982.5 177.2 974.1 179 971.9 177.7 968.6 180.6 964.1 179.9 960.5 182.3 958 181.1 965.3 174.6 969.7 173.2 962.1 172.2 960.8 169.7 965.9 167.8 963.4 164.5 964.4 160.5 971.5 161.1 972.3 157.5 969.2 153.8 969.1 153.7 963.4 152.6 962.3 151 964.1 148.3 962.6 146.6 960 149.5 959.9 143.6 957.7 140.6 959.6 134.4 963.4 129.6 967 130 972.6 129.5 Z"
        ></path>
    </a>
    <a class="{{ greece_status }}" href="{% url 'country' greece.id %}">
        <path
            class="Greece"
            d="M 1112.7 272.6 1115.8 274.8 1119.9 274.4 1123.9 274.8 1123.9 276 1126.7 275.2 1126.2 277.1 1118.6 277.6 1118.5 276.6 1111.9 275.3 1112.7 272.6 Z"
        ></path>
    </a>
    <a class="{{ greece_status }}" href="{% url 'country' greece.id %}">
        <path
            class="Greece"
            d="M 1121.9 239.9 1118.7 239.7 1116 239.1 1109.8 240.7 1113.8 244.3 1111.3 245.4 1108.4 245.4 1105.3 242.1 1104.4 243.5 1106 247.3 1108.9 250.3 1107 251.7 1110.2 254.6 1113 256.5 1113.4 260.1 1108.4 258.4 1110.2 261.7 1106.9 262.3 1109.4 268 1105.9 268.1 1101.3 265.3 1098.9 260.2 1097.6 255.9 1095.3 253 1092.3 249.3 1091.8 247.5 1094 244.4 1094.1 242.3 1095.8 241.4 1095.7 239.7 1099.1 239.2 1100.9 237.8 1103.7 237.9 1104.5 236.8 1105.5 236.6 1109.3 236.8 1113.3 235 1117.2 237.3 1121.8 236.7 1121.5 233.5 1124.2 235.2 1123.1 239.2 1121.9 239.9 Z"
        ></path>
    </a>
    <a class="{{ croatia_status }}" href="{% url 'country' croatia.id %}">
        <path
            d="M1081.5 207.6l1.5 2.5 1.7 1.8-1.7 2.4-2.4-1.4-3.5 0.1-4.5-1.1-2.3 0.1-1 1.4-2-1.5-0.8 2.6 2.7 3 1.3 1.9 2.5 2.4 2.1 1.4 2.1 2.7 4.8 2.4-0.5 1-5-2.3-3.2-2.3-4.8-1.9-4.7-4.6 1-0.5-2.5-2.7-0.3-2.1-3.3-1-1.4 2.7-1.6-2.1 0-2.2 0.1-0.1 3.6 0.2 0.8-1 1.8 1 2 0.1-0.1-1.7 1.7-0.7 0.3-2.5 3.9-1.7 1.6 0.8 4 2.7 4.3 1.2 1.8-1z"
            id="HR"
            name="Croatia"
        ></path>
    </a>
    <a class="{{ hungary_status }}" href="{% url 'country' hungary.id %}">
        <path
            d="M1096.2 191.9l3 1.7 0.5 1.7-2.9 1.3-1.9 4.2-2.6 4.3-3.9 1.2-3.2-0.3-3.7 1.6-1.8 1-4.3-1.2-4-2.7-1.6-0.8-1.2-2.1-0.8-0.1 1.3-4-1.1-1.4 2.8 0 0.2-2.6 2.7 1.7 1.9 0.6 4.1-0.7 0.3-1.3 1.9-0.2 2.3-0.9 0.6 0.4 2.3-0.8 1-1.5 1.6-0.4 5.5 1.9 1-0.6z"
            id="HU"
            name="Hungary"
        ></path>
    </a>
    <a class="{{ ireland_status }}" href="{% url 'country' ireland.id %}">
        <path
            d="M956.7 158.2l0.7 4.4-3.9 5.5-8.8 3.6-6.8-0.9 4.3-6.4-2.1-6.2 6.7-4.8 3.7-2.8 0.9 3.2-1.2 3.3 3-0.1 3.5 1.2z"
            id="IE"
            name="Ireland"
        ></path>
    </a>
    <a class="{{ iceland_status }}" href="{% url 'country' iceland.id %}">
        <path
            d="M924.8 84.5l-1.4 3.6 4.4 3.8-6.1 4.3-13.1 3.9-3.9 1.1-5.6-0.9-11.9-1.8 4.8-2.5-9-2.7 7.9-1.1 0.1-1.7-8.8-1.3 3.6-3.7 6.6-0.8 6 3.8 7-3 5.1 1.5 7.3-2.9 7 0.4z"
            id="IS"
            name="Iceland"
        ></path>
    </a>
    <a class="{{ italy_status }}" href="{% url 'country' italy.id %}">
        <path
            class="Italy"
            d="M 1068.2 256.4 1066.5 261.5 1067.4 263.4 1066.5 266.7 1062.3 264.3 1059.6 263.6 1052.1 260.4 1052.6 257.1 1058.8 257.7 1064.2 257 1068.2 256.4 Z"
        ></path>
    </a>
    <a class="{{ italy_status }}" href="{% url 'country' italy.id %}">
        <path
            class="Italy"
            d="M 1034.2 237.4 1037.5 241.9 1037.1 250.4 1034.7 250 1032.6 252.1 1030.6 250.4 1030.1 242.7 1028.8 239.1 1031.7 239.4 1034.2 237.4 Z"
        ></path>
    </a>
    <a class="{{ italy_status }}" href="{% url 'country' italy.id %}">
        <path
            class="Italy"
            d="M 1055.9 203.9 1055.5 207 1056.9 209.7 1052.8 208.7 1048.9 211 1049.3 214.1 1048.8 215.9 1050.7 219.1 1055.7 222.3 1058.6 227.6 1064.7 232.7 1068.7 232.6 1070.1 234 1068.7 235.3 1073.5 237.6 1077.5 239.5 1082.2 242.9 1082.8 244 1082 246.3 1078.9 243.3 1074.3 242.3 1072.4 246.4 1076.3 248.8 1075.9 252.1 1073.8 252.5 1071.3 258 1069.1 258.5 1069 256.5 1069.9 253.1 1071 251.7 1068.7 248 1066.9 244.8 1064.7 244 1062.9 241.3 1059.5 240.1 1057.1 237.5 1053.3 237.1 1049 234.3 1044.1 230.1 1040.4 226.5 1038.5 220.2 1035.9 219.5 1031.7 217.4 1029.4 218.2 1026.5 221.2 1024.4 221.6 1024.9 218.9 1022.1 218.1 1020.6 213.2 1022.3 211.3 1020.8 208.9 1020.9 207.1 1023.1 208.5 1025.6 208.2 1028.3 206 1029.2 207 1031.6 206.8 1032.6 204.3 1036.4 205.1 1038.5 204 1038.8 201.5 1041.9 202.4 1042.4 201.2 1047.3 200.1 1048.6 202.2 1055.9 203.9 Z"
        ></path>
    </a>
    <a class="{{ lithuania_status }}" href="{% url 'country' lithuania.id %}">
        <path
            d="M1111.1 147.6l1 2.7-3.6 2-0.5 3.4-4.8 2.3-4.7 0-1.4-1.9-2.5-0.7-0.6-1.5 0.2-1.7-2.2-0.9-5.1-1.1-1.7-5.1 5.1-1.8 7.9 0.4 4.5-0.6 0.9 1.2 2.5 0.4 5 2.9z"
            id="LT"
            name="Lithuania"
        ></path>
    </a>
    <a class="{{ luxembourg_status }}" href="{% url 'country' luxembourg.id %}">
        <path
            d="M1016.9 185.4l-1.4 0.1-1.1-0.5 0.4-3.5 1.3-0.2 1 1.4-0.2 2.7z"
            id="LU"
            name="Luxembourg"
        ></path>
    </a>
    <a class="{{ latvia_status }}" href="{% url 'country' latvia.id %}">
        <path
            d="M1112.8 136.5l2.5 1.3 1 2.9 2.1 3.6-4.6 2.3-2.7 1-5-2.9-2.5-0.4-0.9-1.2-4.5 0.6-7.9-0.4-5.1 1.8-0.5-4.5 1.7-3.8 4.1-2 4.4 4.5 3.7-0.2 0.1-4.6 3.8-1 2.1 0.7 4.4 2.2 3.8 0.1z"
            id="LV"
            name="Latvia"
        ></path>
    </a>
    <a class="{{ moldova_status }}" href="{% url 'country' moldova.id %}">
        <path
            d="M1129.4 210.3l-1.3-2.9 0.2-2.7-0.6-2.7-3.4-3.8-2-2.6-1.8-1.8-1.6-0.7 1.1-0.9 3.2-0.6 4 1.9 2 0.3 2.6 1.7-0.1 2.1 2 1 1.1 2.6 2 1.6-0.2 1 1 0.6-1.3 0.5-3-0.2-0.6-0.9-1 0.5 0.6 1.1-1.1 2.1-0.6 2.1-1.2 0.7z"
            id="MD"
            name="Moldova"
        ></path>
    </a>

    <a class="{{ montenegro_status }}" href="{% url 'country' montenegro.id %}">
        <path
            d="M1090.6 227.2l-0.8 1.4-1.4 0.6-0.4-1.2-1.9 3.1 0.5 2.1-1.1-0.5-1.7-2.1-2.3-1.3 0.5-1 0.4-3.5 1.6-1.5 0.9-0.6 1.4 1.1 0.9 0.9 1.7 0.7 2.1 1.3-0.4 0.5z"
            id="ME"
            name="Montenegro"
        ></path>
    </a>
    <a class="{{ norway_status }}" href="{% url 'country' norway.id %}">
        <path
            class="Norway"
            d="M 1113.7 67.5 1107.3 69.6 1104.1 70.1 1104.9 66.3 1099.1 64.2 1093.2 66 1092.1 70 1088.7 72.4 1084 71.1 1078.7 71.3 1073.6 68.5 1071.4 69.9 1068.8 70.1 1068.9 73.7 1060.9 72.8 1060.3 75.9 1056.3 75.9 1054 79.8 1050.6 85.9 1044.9 93.8 1046.7 95.8 1045.4 98 1041.1 97.9 1038.7 103.3 1039.7 111 1042.8 113.9 1042 120.8 1038.6 124.8 1036.8 128.2 1033.5 124.6 1024.9 131.4 1018.8 132.8 1012.3 129.8 1010.5 123.5 1008.5 110 1012.5 106.3 1023.8 101.4 1031.9 95.5 1039.1 87.7 1048 77 1054.4 72.9 1064.7 66.1 1073.2 63.7 1079.9 64 1085.1 59.6 1092.5 59.8 1099.5 58.8 1113.2 62.7 1108.3 64.1 1113.7 67.5 Z"
        ></path>
    </a>
    <a class="{{ norway_status }}" href="{% url 'country' norway.id %}">
        <path
            class="Norway"
            d="M 1076.6 25.2 1069 27.1 1062.2 26 1064.4 24.8 1061.8 23.3 1069.1 22.4 1071 24.1 1076.6 25.2 Z"
        ></path>
    </a>
    <a class="{{ norway_status }}" href="{% url 'country' norway.id %}">
        <path
            class="Norway"
            d="M 1051 16.7 1063.6 20.1 1055 21.9 1053.8 25.3 1050.8 26.2 1049.9 30.2 1045.5 30.4 1037 27.5 1040 25.8 1034.3 24.4 1026.6 20.5 1023.4 17 1032.7 15.4 1035 16.9 1040 16.9 1041 15.4 1046.2 15.2 1051 16.7 Z"
        ></path>
    </a>
    <a class="{{ norway_status }}" href="{% url 'country' norway.id %}">
        <path
            class="Norway"
            d="M 1075.4 13.7 1082.8 15.2 1078.4 17.6 1068.3 18.1 1057.6 17.3 1056.6 16.1 1051.5 16.1 1047.2 14.1 1057.7 12.9 1063.1 13.9 1066.2 12.6 1075.4 13.7 Z"
        ></path>
    </a>

    <a class="{{ poland_status }}" href="{% url 'country' poland.id %}">
        <path
            d="M1079.9 154.8l5.9 0.7 8.8-0.1 2.5 0.7 1.4 1.9 0.6 2.7 1.7 2.3 0.4 2.4-2.8 1.3 1.9 2.8 0.5 2.8 3.2 5.4-0.3 1.7-2.3 0.7-3.8 5.2 1.6 2.8-1.1-0.4-5-2.4-3.5 0.9-2.4-0.6-2.8 1.3-2.7-2.2-1.9 0.9-0.3-0.4-2.6-3.1-3.7-0.3-0.7-2-3.4-0.7-0.6 1.6-2.8-1.3 0.2-1.7-3.7-0.5-2.5-2-2.4-3.9 0.2-2.2-1.5-3.3-1.9-2.1 1.2-1.7-1.4-3.1 3.1-1.8 7.1-2.8 5.8-2 4.8 1 0.6 1.5 4.6 0z"
            id="PL"
            name="Poland"
        ></path>
    </a>
    <a class="{{ romania_status }}" href="{% url 'country' romania.id %}">
        <path
            d="M1118.9 193.1l1.6 0.7 1.8 1.8 2 2.6 3.4 3.8 0.6 2.7-0.2 2.7 1.3 2.9 2.4 1.2 2.3-1.1 2.4 1.1 0.4 1.7-2.3 1.3-1.6-0.6-0.4 7.7-3.1-0.7-4-2.3-5.9 1.5-2.3 1.6-7.6-0.4-4-0.9-1.9 0.4-1.8-2.6-1-1.1 1-1.1-1.3-0.7-1.5 1.4-3.1-1.9-0.7-2.6-3.2-1.4-0.8-2.1-3-2.4 3.9-1.2 2.6-4.3 1.9-4.2 2.9-1.3 2-1.4 3.2 0.7 3.2 0 2.5 1.6 1.6-1 3.6-0.6 1-1.5 2.1 0z"
            id="RO"
            name="Romania"
        ></path>
    </a>
    <a class="{{ serbia_status }}" href="{% url 'country' serbia.id %}">
        <path
            d="M1102 218.2l-1.1 1.4 0.7 2.4 2.8 2.7-1.8 2-0.6 2 0.6 0.8-0.7 0.8-2.4 0.2-1.7 0.3-0.3-0.5 0.6-0.7 0.4-1.6-0.7 0.1-1.1-1.2-0.9-0.3-0.8-1-1-0.4-0.8-0.9-0.9 0.4-0.5 2.1-1.2 0.4 0.4-0.5-2.1-1.3-1.7-0.7-0.9-0.9-1.4-1.1 1.1-0.3 0.5-2.9-2.7-2.5 1.1-2.8-1.9 0.1 1.7-2.4-1.7-1.8-1.5-2.5 3.7-1.6 3.2 0.3 3 2.4 0.8 2.1 3.2 1.4 0.7 2.6 3.1 1.9 1.5-1.4 1.3 0.7-1 1.1 1 1.1z"
            id="RS"
            name="Serbia"
        ></path>
    </a>

    <a class="{{ slovakia_status }}" href="{% url 'country' slovakia.id %}">
        <path
            d="M1098.1 187.7l-1.2 1.7-0.7 2.5-1 0.6-5.5-1.9-1.6 0.4-1 1.5-2.3 0.8-0.6-0.4-2.3 0.9-1.9 0.2-0.3 1.3-4.1 0.7-1.9-0.6-2.7-1.7-0.7-2.1 0.3-0.8 0.6-1.4 2.2 0.1 1.6-0.6 0.1-0.6 0.9-0.3 0.2-1.4 1.1-0.3 0.7-1.1 1.5 0 0.3 0.4 1.9-0.9 2.7 2.2 2.8-1.3 2.4 0.6 3.5-0.9 5 2.4z"
            id="SK"
            name="Slovakia"
        ></path>
    </a>
    <a class="{{ slovenia_status }}" href="{% url 'country' slovenia.id %}">
        <path
            d="M1069.8 203.9l-3.9 1.7-0.3 2.5-1.7 0.7 0.1 1.7-2-0.1-1.8-1-0.8 1-3.6-0.2 1.1-0.5-1.4-2.7 0.4-3.1 4.2 0.5 2.4-1.5 4.4-0.1 0.9-1.1 0.8 0.1 1.2 2.1z"
            id="SI"
            name="Slovenia"
        ></path>
    </a>
    <a class="{{ sweden_status }}" href="{% url 'country' sweden.id %}">
        <path
            d="M1088.2 87l-7 1.6-3.5 3.9 1.3 3.5-6.2 4.5-7.8 5-2.1 8.1 3.7 4.1 4.8 3.3-3.3 6.6-4.6 1.4-0.6 10-2.1 5.7-5.7-0.6-2.2 4.8-5.5 0.3-1.9-5.7-4.5-6.9-4.2-8.4 1.8-3.4 3.4-4 0.8-6.9-3.1-2.9-1-7.7 2.4-5.4 4.3 0.1 1.3-2.2-1.8-2 5.7-7.9 3.4-6.1 2.3-3.9 4 0 0.6-3.1 8 0.9-0.1-3.6 2.6-0.2 6 2.7 7.2 3.7 1.8 8.5 1.8 2.2z"
            id="SE"
            name="Sweden"
        ></path>
    </a>
    <a class="{{ ukraine_status }}" href="{% url 'country' ukraine.id %}">
        <path
            d="M1157.2 174.6l2.3 2.7 0.1 1.2 6.7 2.2 3.6-1 3.6 2.9 2.9-0.1 7.7 2 0.4 1.9-1.3 3.2 1.8 3.5-0.3 2.1-4.8 0.4-2.2 1.8 0.4 2.7-3.9 0.5-3 2.1-4.6 0.3-4 2.4 1 3.9 2.8 1.5 5.1-0.4-0.6 2.3-5.4 1.1-6.3 3.6-3.1-1.3 0.7-2.9-5.9-1.9 0.7-1.2 4.6-2.1-1.7-1.4-8.1-1.6-0.8-2.4-4.5 0.8-1.3 3.5-3.3 4.6-2.4-1.1-2.3 1.1-2.4-1.2 1.2-0.7 0.6-2.1 1.1-2.1-0.6-1.1 1-0.5 0.6 0.9 3 0.2 1.3-0.5-1-0.6 0.2-1-2-1.6-1.1-2.6-2-1 0.1-2.1-2.6-1.7-2-0.3-4-1.9-3.2 0.6-1.1 0.9-2.1 0-1 1.5-3.6 0.6-1.6 1-2.5-1.6-3.2 0-3.2-0.7-2 1.4-0.5-1.7-3-1.7 0.7-2.5 1.2-1.7 1.1 0.4-1.6-2.8 3.8-5.2 2.3-0.7 0.3-1.7-3.2-5.4 2.3-0.3 2.4-1.6 3.8-0.2 4.9 0.5 5.7 1.5 3.9 0.1 1.9 0.9 1.7-1.1 1.5 1.5 4.3-0.3 2.1 0.6-0.3-3.1 1.3-1.4 4.1-0.3 1.8 0.2 1-1.4 1.5 0.3 4.9-0.6 3.8 3.5-0.9 1.3 0.8 1.9 3.9 0.3z"
            id="UA"
            name="Ukraine"
        ></path>
    </a>
    <a class="{{ netherlands_status }}" href="{% url 'country' netherlands.id %}">
        <path
            d="M1016.5 177.1l-2.8-1.5-3.1-2.7-4.5 1.3-3.6-0.5 2.5-1.7 4-9 6.5-2.6 4 0.2 0.9 2.1-0.9 5.6-1.2 2.3-2.9 0 1.1 6.5z"
            id="NL"
            name="Netherlands"
        ></path>
    </a>
    <a class="{{ portugal_status }}" href="{% url 'country' portugal.id %}">
        <path
            d="M946.9 263.7l-2.2 1.6-2.8-0.9-2.7 0.7 0.9-5-0.3-3.9-2.4-0.6-1.1-2.4 0.5-4.2 2.2-2.3 0.5-2.6 1.2-3.8 0-2.7-0.9-2.3-0.2-2.2 1.9-1.6 2.2-0.9 1.2 3.1 3 0 0.9-0.8 3.1 0.2 1.3 3.2-2.4 1.7-0.3 5-0.8 0.9-0.3 3.1-2.3 0.5 2 3.8-1.6 4.2 1.8 1.9-0.8 1.7-2 2.4 0.4 2.2z"
            id="PT"
            name="Portugal"
        ></path>
    </a>

    <a class="{{ spain_status }}" href="{% url 'country' spain.id %}">
        <path
            d="M976.6 223.4l2 2.4 9.5 2.9 1.9-1.4 5.8 2.9 5.9-0.8 0.4 3.7-4.9 4.2-6.6 1.4-0.5 2.1-3.2 3.5-2 5.2 2 3.7-3 2.8-1.2 4.2-4 1.3-3.7 4.9-6.8 0.1-5-0.1-3.4 2.2-2.1 2.4-2.6-0.5-1.9-2.2-1.4-3.6-4.9-1-0.4-2.2 2-2.4 0.8-1.7-1.8-1.9 1.6-4.2-2-3.8 2.3-0.5 0.3-3.1 0.8-0.9 0.3-5 2.4-1.7-1.3-3.2-3.1-0.2-0.9 0.8-3 0-1.2-3.1-2.2 0.9-1.9 1.6 0.5-4.5-2-2.7 7.4-4.6 6.2 1.1 6.9 0 5.4 1.1 4.3-0.4 8.3 0.3z"
            id="ES"
            name="Spain"
        ></path>
    </a>
    <a class="{{ france_status }}" href="{% url 'country' france.id %}">
        <path
            class="France"
            d="M 1035.7 231.4 1034.2 236.3 1031.8 235 1030.5 230.8 1031.4 228.4 1034.6 226 1035.7 231.4 Z"
        ></path>
    </a>
    <a class="{{ france_status }}" href="{% url 'country' france.id %}">
        <path
            class="France"
            d="M 1014.4 185 1015.5 185.5 1016.9 185.4 1019.3 187 1026.5 188.2 1024.1 192.4 1023.7 196.9 1022.4 198 1020.1 197.4 1020.3 199 1016.7 202.5 1016.7 205.4 1019.1 204.4 1020.9 207.1 1020.8 208.9 1022.3 211.3 1020.6 213.2 1022.1 218.1 1024.9 218.9 1024.4 221.6 1019.9 225.2 1009.7 223.5 1002.3 225.6 1001.7 229.4 995.8 230.2 990 227.3 988.1 228.7 978.6 225.8 976.6 223.4 979.3 219.6 980.3 207 975.2 200.4 971.5 197.2 963.9 194.8 963.5 190.2 970 188.9 978.3 190.5 976.8 183.4 981.5 186.1 992.9 181.3 994.4 176.2 998.6 174.9 999.4 177.1 1001.6 177.2 1004 179.7 1007.5 182.6 1010 182.1 1014.4 185 Z"
        ></path>
    </a>
    <a class="{{ malta_status }}" href="{% url 'country' malta.id %}">
        <path
            class="Malta"
            d="M 1063.9 271.7 1063.7 272 1063.2 271.8 1062.7 271.5 1062.7 271 1062.6 270.9 1063.2 270.9 1063.6 271.2 1063.8 271.4 1063.9 271.7 Z"
        ></path>
    </a>
    <a class="{{ malta_status }}" href="{% url 'country' malta.id %}">
        <path
            class="Malta"
            d="M 1062.3 270.6 1061.8 270.5 1061.8 270.3 1062.2 270.2 1062.6 270.5 1062.3 270.6 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 888.4 323.4 888.1 323.9 887.7 324.4 887.4 324 887 324 886.8 323.8 887 323.5 887.4 323.6 887.8 323.2 888.1 323 888.3 323.1 888.4 323.4 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 902 321.1 902 321.6 902.2 322 902 322.7 902.1 323 901.7 323.4 901.2 323.6 901 323.8 900.4 323.6 899.9 323.1 899.7 322.7 899.7 322.1 900.3 321.7 900.4 321.2 900.4 321 901 321.1 901.4 321.1 901.7 321.2 902 321.1 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 892.1 321.9 891.9 321.9 891.6 321.7 891.4 321.4 891.5 321 891.6 320.7 891.9 320.7 892.2 320.7 892.7 321.1 892.8 321.4 892.3 321.9 892.1 321.9 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 898.2 318.4 898.2 318.6 897.6 318.9 897.2 319.4 896.9 319.6 896.9 320 896.5 320.7 896.4 321.1 895.9 321.7 895.8 321.9 895.6 321.9 895 322.1 894.9 322 894.8 321.6 894.5 321.2 894.4 321 894.2 320.7 894.2 320.4 893.8 319.8 894.3 319.5 894.6 319.7 895.2 319.5 895.6 319.5 896.1 319.3 896.6 318.9 896.6 318.7 897.2 318.4 897.8 318.4 898.1 318.3 898.2 318.4 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 908.4 321.2 908.1 321.6 907.7 321.7 907.4 321.6 907 321.6 907 321.4 907.3 321.4 907.9 321.2 908.3 320.9 908.6 320.6 908.7 320.1 908.8 319.8 909 319.3 909.3 318.9 909.6 318.3 909.8 317.5 910 317.3 910.4 317.2 910.7 317.5 910.8 318 910.7 318.5 910.6 319 910.6 319.5 910.5 319.6 910.2 320.3 909.9 320.6 909.3 320.7 908.6 321 908.4 321.2 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 888.8 316.7 889.1 316.6 889.3 316.9 889.5 317.4 889.3 317.7 889.4 318.1 888.8 319.1 888.7 319 888.6 318.6 888.2 317.7 888.1 317.4 888 317.2 888.2 316.8 888.5 316.6 888.8 316.7 Z"
        ></path>
    </a>
    <a class="{{ canary_islands_status }}" href="{% url 'country' canary_islands.id %}">
        <path
            class="Canary Islands (Spain)"
            d="M 912.9 314.7 912.9 315.1 912.7 315.6 912 316.1 911.5 316.2 911.1 316.7 910.6 316.5 910.6 316.4 910.8 316 910.8 315.6 911 315.3 911.3 315.1 911.6 315.1 911.9 314.8 912.4 314.8 912.5 314.7 912.7 314.2 912.9 314.1 913.1 314.3 912.9 314.7 Z"
        ></path>
    </a>
    <circle cx="997.9" cy="189.1" id="0"></circle>
    <circle cx="673.5" cy="724.1" id="1"></circle>
    <circle cx="1798.2" cy="719.3" id="2"></circle>
  </svg>

</div>

{% endblock content %}
