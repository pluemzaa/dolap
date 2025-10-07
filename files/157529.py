<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="LAP1fi"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:12:43 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NTc6MTggUE07MjU4Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDc6MTI6NDMgUE07NjsyNjkx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Coffee, Tea, menu, qua, teai, coffeei, poop" type="Integer" array="False" size=""/>
            <assign variable="Coffee" expression="10"/>
            <assign variable="Tea" expression="0"/>
            <assign variable="teai" expression="20"/>
            <assign variable="coffeei" expression="25"/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: &quot;&amp; coffee &amp;&quot;&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: &quot;&amp; Tea &amp;&quot;&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu == 1">
                <then>
                    <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                    <input variable="qua"/>
                    <if expression="qua &gt;= 11">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <assign variable="poop" expression="coffeei * qua"/>
                            <output expression="&quot;Total Price : &quot;&amp;poop&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="menu == 2">
                        <then>
                            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
                            <input variable="qua"/>
                            <if expression="qua &gt;= 0">
                                <then>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <assign variable="poop" expression="Teai * qua"/>
                                    <output expression="&quot;Total Price : &quot;&amp;poop&amp;&quot; Baht&quot;" newline="True"/>
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