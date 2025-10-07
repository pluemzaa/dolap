<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab44"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 10:47:43 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NDQ6MjUgUE07MjU3OA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTY6MzAgUE07MzsyNjg3"/>
        <attribute name="edited" value="VXNlcjtNSUROSUdIVDsyNTY4LTA3LTE2OzEwOjQ3OjQzIFBNOzE7MjQxNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="y, p, i, total" type="Integer" array="False" size=""/>
            <declare name="money" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="p"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="y"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; y">
                <output expression="&quot;Year &quot; &amp; (i+1) &amp; &quot;:&quot;" newline="False"/>
                <assign variable="money" expression="money * (1 + (p / 100))"/>
                <output expression="money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>