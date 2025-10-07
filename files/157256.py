<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lap4.2"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 02:20:34 AM"/>
        <attribute name="created" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE3OzAxOjM0OjAxIEFNOzMwMTE="/>
        <attribute name="edited" value="TGVub3ZvO0RFU0tUT1AtTFRVR0FETjsyNTY4LTA3LTE3OzAyOjIwOjM0IEFNOzExOzMxNzA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="choose, Stock" type="Integer" array="False" size=""/>
            <declare name="coffee, Total" type="Real" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <assign variable="coffee" expression="25"/>
            <input variable="choose"/>
            <if expression="choose == 1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="Stock"/>
                    <if expression="Stock &lt;= 10">
                        <then>
                            <assign variable="Total" expression="coffee * Stock"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp; Total &amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="Stock"/>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>