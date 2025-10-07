<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Coffee"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:26:42 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MjA6NDcgUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6Mzg6MTAgUE07MTtjb21wdXRlcjtDUC1DT007MjAyNS0wNy0xNjswMToyNDowMCBQTTtsYWI0X3Rlc3QyLmZwcmc7Njc5NA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MjY6NDIgUE07NjsyNjk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, quantity, total" type="Integer" array="False" size=""/>
            <declare name="cQty, tQty" type="Integer" array="False" size=""/>
            <assign variable="cQty" expression="10"/>
            <assign variable="tQty" expression="0"/>
            <output expression="&quot;Beverage List: &quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="quantity"/>
            <input variable="total"/>
            <input variable="menu"/>
            <if expression="menu = 1">
                <then>
                    <if expression="cQty &gt; quantity">
                        <then>
                            <assign variable="total" expression="quantity*25"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot;Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu = 2">
                        <then>
                            <if expression="tQty &gt; quantity">
                                <then>
                                    <assign variable="total" expression="quantity*20"/>
                                    <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot;Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </else>
                            </if>
                        </then>
                        <else>
                            <output expression="&quot;invalid menu&quot;" newline="True"/>
                        </else>
                    </if>
                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>