<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.4"/>
        <attribute name="authors" value="Windows11"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 04:53:30 PM"/>
        <attribute name="created" value="V2luZG93czExO01TSTsyNTY4LTA3LTE3OzAzOjE2OjE1IFBNOzIzNzQ="/>
        <attribute name="edited" value="V2luZG93czExO01TSTsyNTY4LTA3LTE3OzA0OjUzOjMwIFBNOzQ7MjQ4NA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, years, i, year1, Year2, Year3, total" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="total" expression="money"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=years">
                <assign variable="total" expression="total*(1+interest/100)"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>