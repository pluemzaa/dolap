<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_402"/>
        <attribute name="authors" value="K"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 09:15:27 AM"/>
        <attribute name="created" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xODswODowMTozNCBBTTsyNDI4"/>
        <attribute name="edited" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xODswOToxNToyNyBBTTs1OzI1NDg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Beverage List:&quot;" newline="True"/>
            <output expression="&quot;1. Coffee - 25 Baht - Qty: 10&quot;" newline="True"/>
            <output expression="&quot;2. Tea - 20 Baht - Qty: 0&quot;" newline="True"/>
            <declare name="select, king" type="Integer" array="False" size=""/>
            <output expression="&quot;Select menu (1 = Coffee, 2 = Tea):&quot;" newline="True"/>
            <input variable="select"/>
            <output expression="&quot;Enter quantity:&quot;" newline="True"/>
            <input variable="king"/>
            <if expression="select = 1">
                <then>
                    <if expression="king &gt; 10">
                        <then>
                            <output expression="&quot;Sorry, Coffee out of stock&quot;" newline="True"/>
                        </then>
                        <else>
                            <output expression="&quot;You purchased Coffee&quot;" newline="True"/>
                            <output expression="&quot;Total Price : &quot; &amp;&#10;25 * king&#10;&amp; &quot; Baht&quot;" newline="True"/>
                            <output expression="&quot;Enjoy!&quot;" newline="True"/>
                        </else>
                    </if>
                </then>
                <else>
                    <output expression="&quot;Sorry, Tea out of stock&quot;" newline="True"/>
                </else>
            </if>
        </body>
    </function>
</flowgorithm>