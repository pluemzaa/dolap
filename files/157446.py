<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4"/>
        <attribute name="authors" value="Windows10"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 12:37:52 PM"/>
        <attribute name="created" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE4OzA5OjQ5OjAxIFBNOzMyNDQ="/>
        <attribute name="edited" value="V2luZG93czEwO0RFU0tUT1AtSEpRNVVTQTsyNTY4LTA3LTE5OzEyOjM3OjUyIFBNOzg7MzM1Nw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="interest" expression="interest/100"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=years">
                <assign variable="money" expression="money * (1+ interest)"/>
                <output expression="&quot;Year &quot;&amp; i &amp;&quot;:&quot;&amp; money &amp;&quot; &quot;" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>