<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowlab4"/>
        <attribute name="authors" value="Nattakrit"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 01:25:26 PM"/>
        <attribute name="created" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzEwOjMxOjMxIEFNOzMwODY="/>
        <attribute name="edited" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzAxOjI1OjI2IFBNOzQ7MzIxOQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, qua" type="Integer" array="False" size=""/>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea): &quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Enter quantity: &quot;" newline="True"/>
            <input variable="qua"/>
            <if expression="s==1">
                <then>
                    <if expression="qua&lt;=10">
                        <then>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot;&amp; (qua*25)&amp;&quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <if expression="s==2">
                        <then>
                            <if expression="qua&lt;0">
                                <then>
                                    <output expression="&quot;You purchased Tea&quot;" newline="True"/>
                                    <output expression="&quot;Total Price : &quot;&amp; (qua*20)&amp;&quot; Baht&quot;" newline="True"/>
                                    <output expression="&quot;Enjoy!&quot;" newline="True"/>
                                </then>
                                <else>
                                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
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