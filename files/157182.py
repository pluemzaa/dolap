<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test2_lab4"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:33:45 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MjU6MDUgUE07MjU3OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MzM6NDUgUE07MTsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="menu" type="Integer" array="False" size=""/>
            <output expression="&quot;Pleas select&quot;" newline="True"/>
            <output expression="&quot;1 Coke&quot;" newline="True"/>
            <output expression="&quot;2 pepsi&quot;" newline="True"/>
            <input variable="menu"/>
            <if expression="menu==1">
                <then>
                    <output expression="&quot;You selected Coke&quot;" newline="True"/>
                    <output expression="&quot;Price : 25 Bant&quot;" newline="True"/>
                </then>
                <else>
                    <if expression="menu==2">
                        <then>
                            <output expression="&quot;Y[o selected pepsi&quot;" newline="True"/>
                            <output expression="&quot;Price : 15 Bant&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;invalid menu&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>