<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="001"/>
        <attribute name="authors" value="USER"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 03:29:15 PM"/>
        <attribute name="created" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzoxNDo1NiBQTTsyNjgz"/>
        <attribute name="edited" value="VVNFUjtERVNLVE9QLVBQREtFMUk7MjAyNS0wNy0xNzswMzoyOToxNSBQTTsxOzI3OTI="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, CFPrice, TPrice, Ko" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==2">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="Ko"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </then>
                <else>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="Ko"/>
                    <if expression="Ko&lt;=10">
                        <then>
                            <assign variable="Ko" expression="Ko*25"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot; &amp;Ko&amp;  &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>