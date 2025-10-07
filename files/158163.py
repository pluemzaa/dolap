<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flow5"/>
        <attribute name="authors" value="TUF Gaming F15"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 09:57:58 PM"/>
        <attribute name="created" value="VFVGIEdhbWluZyBGMTU7REVTS1RPUC03UFBINkxWOzI1NjgtMDctMjE7MDk6Mzc6MzIgUE07MzQ1NQ=="/>
        <attribute name="edited" value="VFVGIEdhbWluZyBGMTU7REVTS1RPUC03UFBINkxWOzI1NjgtMDctMjE7MDk6NDg6MjggUE07MTszNTcw"/>
        <attribute name="edited" value="dXNFcjtPTkRFU09HT09EOzIwMjUtMDctMjE7MDk6NTc6NTggUE07NDsyNTc2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu, qty, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qty"/>
            <if expression="menu == 1">
                <then>
                    <if expression="qty &lt;= 10">
                        <then>
                            <assign variable="total" expression="qty * 25"/>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;total&amp; &quot; Baht &quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else/>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>