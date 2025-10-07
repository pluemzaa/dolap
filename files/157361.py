<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 07:25:36 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjoyMDo1NyBQTTsyNTQ1"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xNzswMjozMTo1OSBQTTsxOzI2NTc="/>
        <attribute name="edited" value="cG9vcmk7UE9PUklQQVQ7MjAyNS0wNy0xNzswNzoyNTozNiBQTTsxOzI1NzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="t, c, menu" type="Integer" array="False" size=""/>
            <assign variable="c" expression="10"/>
            <assign variable="t" expression="0"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1.Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <output expression="&quot;Enter quantity:&quot;" newline="True"/>
                    <input variable="c"/>
                    <if expression="c &lt;= 10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price: &quot;&amp; 25*c &amp; &quot; Baht&quot;" newline="True"/>
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
                            <input variable="t"/>
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