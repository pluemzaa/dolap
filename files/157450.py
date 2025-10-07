<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_404"/>
        <attribute name="authors" value="K"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 12:55:43 PM"/>
        <attribute name="created" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xOTsxMDowNzo0MyBBTTsyNDI4"/>
        <attribute name="edited" value="SztERVNLVE9QLTY1TEZVTEo7MjU2OC0wNy0xOTsxMjo1NTo0MyBQTTszOzI1NTg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money" type="Real" array="False" size=""/>
            <declare name="inter, year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <for variable="i" start="1" end="year" direction="inc" step="1">
                <assign variable="money" expression="money * (1 + inter/100)"/>
                <output expression="&quot;Year&quot; &amp;i&amp;&quot;:&quot; &amp; money" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>