<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="ex2"/>
        <attribute name="authors" value="MY COM"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 11:04:22 PM"/>
        <attribute name="created" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE2OzA4OjQ2OjA1IFBNOzI3Njc="/>
        <attribute name="edited" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE2OzExOjA0OjIyIFBNOzEzOzI5MTM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="tea, coff, menu" type="Integer" array="False" size=""/>
            <assign variable="coff" expression="10"/>
            <assign variable="tea" expression="0"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1.Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2.Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="coff"/>
                    <if expression="coff &lt;= 10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price: &quot;&amp; 25*coff&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="tea"/>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>