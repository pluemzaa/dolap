<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab.3"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 10:22:03 PM"/>
        <attribute name="created" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MDg6MTY6NTUgUE07MjkxOQ=="/>
        <attribute name="edited" value="QWRtaW47REVTS1RPUC1GRVNPSFVUOzI1NjgtMDctMTc7MTA6MjI6MDMgUE07MzszMDEy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest, money" type="Real" array="False" size=""/>
            <declare name="years, n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=years">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;year&quot;&amp;i&amp;&quot;:&quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>