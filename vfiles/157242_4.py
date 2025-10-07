<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3585;&#3634;&#3648;&#3648;&#3615;"/>
        <attribute name="authors" value="ASUS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 09:41:57 PM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xNjswOToxMToxMCBQTTsyNzAx"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtTVVIVTVGSEc7MjU2OC0wNy0xNjswOTo0MTo1NyBQTTsxOzI4MjM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, menu, eq, Total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="eq"/>
            <if expression="menu == 1">
                <then>
                    <if expression="eq &lt;= 10">
                        <then>
                            <assign variable="Total" expression="eq * 25"/>
                            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;  &amp;menu" newline="True"/>
                            <output expression="&quot;Enter quantity:&quot;&amp;eq" newline="True"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price :&quot; &amp;Total" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="eq == 0">
                        <then>
                            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;  &amp;menu" newline="True"/>
                            <output expression="&quot;Enter quantity:&quot;&amp;eq" newline="True"/>
                            <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                            <output expression="&quot;Total Price : 20&quot;" newline="True"/>
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