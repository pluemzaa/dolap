<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test2"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:31:51 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MTM6MzkgUE07MjU3OQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MzE6NTEgUE07MzsyNjgz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="M, Q, total, CQ, TQ, CP, TP" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <assign variable="CP" expression="25"/>
            <assign variable="CQ" expression="10"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <assign variable="TP" expression="20"/>
            <assign variable="TQ" expression="0"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="M"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="Q"/>
            <if expression="M==1">
                <then>
                    <if expression="Q&gt;10">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <if expression="Q&lt;1">
                                <then>
                                    <output expression="&quot;Error&quot;" newline="True"/>
                                </then>
                                <else>
                                    <assign variable="total" expression="Q*CP"/>
                                    <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot;&amp; total &amp;&quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </else>
                            </if>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="M==2">
                        <then>
                            <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Error&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>