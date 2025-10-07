<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:36:51 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTI6MzUgUE07MjU3NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTI6MzcgUE07MTtjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswMTo1Nzo1NyBQTTtsYWI0XzEuZnByZzs2MzY0"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MzY6NTEgUE07MTsyNjg2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="coffee, tea, selectMenu, qty, total1, total2" type="Integer" array="False" size=""/>
            <assign variable="coffee" expression="25"/>
            <assign variable="tea" expression="20"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="selectMenu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qty"/>
            <assign variable="total1" expression="coffee * qty"/>
            <assign variable="total2" expression="tea * qty"/>
            <if expression="selectMenu == 1">
                <then>
                    <if expression="qty &gt; 10">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;total1&amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="selectMenu == 2">
                        <then>
                            <if expression="qty &gt;= 0">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot; &amp;total2&amp; &quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>